import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import os

# ════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="🛒 Shopper Spectrum",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ════════════════════════════════════════════════════════════════
# CUSTOM CSS - PREMIUM STYLING
# ════════════════════════════════════════════════════════════════
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 25px;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
    }
    
    .segment-card {
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid;
        background: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    
    .high-value {
        border-left-color: #2ca02c;
        background: linear-gradient(90deg, #f0fff4 0%, white 100%);
    }
    
    .regular {
        border-left-color: #1f77b4;
        background: linear-gradient(90deg, #f0f4ff 0%, white 100%);
    }
    
    .atrisk {
        border-left-color: #d62728;
        background: linear-gradient(90deg, #fff5f5 0%, white 100%);
    }
    
    .occasional {
        border-left-color: #ff7f0e;
        background: linear-gradient(90deg, #fff9f0 0%, white 100%);
    }
    
    .header-title {
        font-size: 3em;
        font-weight: bold;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 30px 0;
    }
    
    .subheader-text {
        text-align: center;
        color: #666;
        font-size: 1.2em;
        margin-bottom: 30px;
    }
    
    .stat-box {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        text-align: center;
    }
    
    .stat-number {
        font-size: 2.5em;
        font-weight: bold;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stat-label {
        color: #999;
        font-size: 0.9em;
        margin-top: 10px;
    }
    
    hr {
        margin: 30px 0;
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
    }
</style>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# LOAD MODELS & DATA
# ════════════════════════════════════════════════════════════════
@st.cache_resource
def load_models():
    kmeans = joblib.load('models/kmeans_model.pkl')
    scaler = joblib.load('models/rfm_scaler.pkl')
    return kmeans, scaler

@st.cache_data
def load_data():
    rfm_data = pd.read_csv('models/rfm_with_clusters.csv')
    all_products = joblib.load('models/all_products.pkl')
    product_sim_df = pd.read_csv('models/product_similarity.csv', index_col=0)
    return rfm_data, all_products, product_sim_df

models_dir = "models"
required_files = [
    "kmeans_model.pkl", "rfm_scaler.pkl", 
    "rfm_with_clusters.csv", "all_products.pkl", 
    "product_similarity.csv"
]

missing_files = [f for f in required_files if not os.path.exists(os.path.join(models_dir, f))]

if missing_files:
    st.error(f"❌ Missing: {', '.join(missing_files)}\nRun Jupyter notebook first!")
    st.stop()

try:
    kmeans, scaler = load_models()
    rfm_data, all_products, product_sim_df = load_data()
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

# ════════════════════════════════════════════════════════════════
# CLUSTER CONFIGURATION
# ════════════════════════════════════════════════════════════════
segment_info = {
    0: {
        'name': 'Regular Customer 🙂',
        'color': '#1f77b4',
        'emoji': '🙂',
        'description': 'Steady purchasers with moderate spending',
        'strategy': '📧 Send regular newsletters and moderate seasonal discounts',
        'icon': '📊'
    },
    1: {
        'name': 'High-Value Customer 👑',
        'color': '#2ca02c',
        'emoji': '👑',
        'description': 'Premium customers - frequent & big spenders',
        'strategy': '🎁 Reward with loyalty points, VIP access, and exclusive offers',
        'icon': '⭐'
    },
    2: {
        'name': 'At-Risk Customer ⚠️',
        'color': '#d62728',
        'emoji': '⚠️',
        'description': "Haven't purchased recently",
        'strategy': '🚨 Send win-back campaigns with personalized offers urgently',
        'icon': '🔔'
    },
    3: {
        'name': 'Occasional Customer 😐',
        'color': '#ff7f0e',
        'emoji': '😐',
        'description': 'Rare, occasional purchases',
        'strategy': '🎯 Re-engage with limited-time special offers',
        'icon': '🎯'
    }
}

# ════════════════════════════════════════════════════════════════
# HEADER
# ════════════════════════════════════════════════════════════════
st.markdown('<div class="header-title">🛒 SHOPPER SPECTRUM</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader-text">Customer Intelligence & Product Recommendation Engine</div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# SIDEBAR
# ════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("---")
    page = st.radio(
        "**📍 Navigate to**",
        ["🏠 Dashboard", "🔍 Segment Predictor", "🎯 Product Finder", "📈 Analytics"],
        help="Choose a page to explore"
    )
    st.markdown("---")
    st.info("""
    **⚡ Quick Info:**
    - **Customers**: 4,338
    - **Products**: 3,877
    - **Segments**: 4
    - **Algorithm**: KMeans
    """)

# ════════════════════════════════════════════════════════════════
# PAGE 1: DASHBOARD
# ════════════════════════════════════════════════════════════════
if page == "🏠 Dashboard":
    # Key Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">4,338</div>
            <div class="stat-label">Total Customers</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">3,877</div>
            <div class="stat-label">Products</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">4</div>
            <div class="stat-label">Segments</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">500K+</div>
            <div class="stat-label">Transactions</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Segment Distribution
    col1, col2 = st.columns(2)
    
    with col1:
        segment_counts = rfm_data['Segment'].value_counts()
        fig_pie = go.Figure(data=[
            go.Pie(
                labels=segment_counts.index,
                values=segment_counts.values,
                hole=0.4,
                marker=dict(colors=['#2ca02c', '#1f77b4', '#d62728', '#ff7f0e']),
                textinfo="label+percent",
                hovertemplate="<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>"
            )
        ])
        fig_pie.update_layout(
            title="<b>Customer Segment Distribution</b>",
            height=400,
            showlegend=True,
            font=dict(size=12)
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        segment_counts = rfm_data['Segment'].value_counts()
        colors_map = {'High-Value': '#2ca02c', 'Regular': '#1f77b4', 'At-Risk': '#d62728', 'Occasional': '#ff7f0e'}
        fig_bar = go.Figure(data=[
            go.Bar(
                x=segment_counts.index,
                y=segment_counts.values,
                marker=dict(color=[colors_map.get(s, '#999') for s in segment_counts.index]),
                text=segment_counts.values,
                textposition='outside',
                hovertemplate="<b>%{x}</b><br>Customers: %{y}<extra></extra>"
            )
        ])
        fig_bar.update_layout(
            title="<b>Segment Count</b>",
            xaxis_title="Segment",
            yaxis_title="Number of Customers",
            height=400,
            showlegend=False,
            font=dict(size=12)
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    
    st.markdown("---")
    
    # RFM Metrics
    st.subheader("📊 RFM Metrics by Segment")
    
    segment_stats = rfm_data.groupby('Segment')[['Recency', 'Frequency', 'Monetary']].mean()
    
    fig_rfm = go.Figure()
    fig_rfm.add_trace(go.Bar(x=segment_stats.index, y=segment_stats['Recency'], name='Avg Recency (days)', marker_color='#667eea'))
    fig_rfm.add_trace(go.Bar(x=segment_stats.index, y=segment_stats['Frequency'], name='Avg Frequency', marker_color='#764ba2'))
    fig_rfm.add_trace(go.Bar(x=segment_stats.index, y=segment_stats['Monetary']/100, name='Avg Monetary (£/100)', marker_color='#f093fb'))
    
    fig_rfm.update_layout(
        title="<b>RFM Metrics Comparison</b>",
        barmode='group',
        height=400,
        hovermode='x unified',
        font=dict(size=11)
    )
    st.plotly_chart(fig_rfm, use_container_width=True)

# ════════════════════════════════════════════════════════════════
# PAGE 2: SEGMENT PREDICTOR
# ════════════════════════════════════════════════════════════════
elif page == "🔍 Segment Predictor":
    st.markdown('<div class="header-title" style="font-size: 2em;">🔍 Predict Customer Segment</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        recency = st.number_input("📅 Recency (days since last purchase)", min_value=0, max_value=1000, value=30)
    with col2:
        frequency = st.number_input("🛍️ Frequency (number of purchases)", min_value=0, max_value=500, value=5)
    with col3:
        monetary = st.number_input("💰 Monetary (total spend in £)", min_value=0.0, max_value=100000.0, value=500.0)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🚀 PREDICT SEGMENT", use_container_width=True, type="primary"):
            input_data = np.array([[recency, frequency, monetary]])
            scaled_input = scaler.transform(input_data)
            cluster = kmeans.predict(scaled_input)[0]
            
            segment = segment_info[cluster]
            
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, {segment["color"]} 0%, {segment["color"]}cc 100%);
                        padding: 40px; border-radius: 20px; text-align: center;
                        margin: 20px 0; color: white; box-shadow: 0 10px 40px rgba(0,0,0,0.2);'>
                <div style='font-size: 3em; margin-bottom: 10px;'>{segment["emoji"]}</div>
                <h2 style='margin: 0; font-size: 2.5em;'>{segment["name"]}</h2>
                <p style='margin-top: 15px; font-size: 1.1em; opacity: 0.95;'>{segment["description"]}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.success(f"### 💡 Recommended Strategy\n{segment['strategy']}")
            
            # Segment comparison
            st.markdown("---")
            st.subheader("📊 How This Customer Compares")
            
            col1, col2, col3 = st.columns(3)
            
            segment_avg = rfm_data[rfm_data['Segment'] == segment['name']].mean()
            
            with col1:
                st.metric(
                    "Recency vs Segment Avg",
                    f"{recency} days",
                    f"{recency - segment_avg['Recency']:.0f} days",
                    delta_color="inverse"
                )
            
            with col2:
                st.metric(
                    "Frequency vs Segment Avg",
                    f"{frequency} purchases",
                    f"{frequency - segment_avg['Frequency']:.1f}",
                    delta_color="normal"
                )
            
            with col3:
                st.metric(
                    "Monetary vs Segment Avg",
                    f"£{monetary:.2f}",
                    f"£{monetary - segment_avg['Monetary']:.2f}",
                    delta_color="normal"
                )

# ════════════════════════════════════════════════════════════════
# PAGE 3: PRODUCT FINDER
# ════════════════════════════════════════════════════════════════
elif page == "🎯 Product Finder":
    st.markdown('<div class="header-title" style="font-size: 2em;">🎯 Discover Similar Products</div>', unsafe_allow_html=True)
    
    product_input = st.selectbox(
        "🔍 **Search or select a product**",
        options=sorted(all_products),
        help="Type to filter products"
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("✨ GET RECOMMENDATIONS", use_container_width=True, type="primary"):
            if product_input:
                product_input = product_input.upper().strip()
                
                if product_input in product_sim_df.index:
                    similar = product_sim_df[product_input].sort_values(ascending=False)[1:6]
                    
                    st.success("✅ **Top 5 Similar Products**", icon="✅")
                    st.markdown("---")
                    
                    for i, (product, score) in enumerate(similar.items(), 1):
                        col1, col2 = st.columns([4, 1])
                        
                        with col1:
                            st.markdown(f"""
                            <div class="segment-card high-value" style="border-left-color: #667eea;">
                                <div style="font-size: 1.1em; font-weight: bold;">
                                    #{i} {product}
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col2:
                            st.metric("Match", f"{score*100:.1f}%")
                else:
                    st.error("❌ Product not found. Try another one!")

# ════════════════════════════════════════════════════════════════
# PAGE 4: ANALYTICS
# ════════════════════════════════════════════════════════════════
elif page == "📈 Analytics":
    st.markdown('<div class="header-title" style="font-size: 2em;">📈 Detailed Analytics</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📊 Segment Profiles", "🎯 RFM Analysis", "💡 Business Insights"])
    
    with tab1:
        st.subheader("Segment Characteristics")
        
        for segment_name in ['High-Value', 'Regular', 'At-Risk', 'Occasional']:
            segment_data = rfm_data[rfm_data['Segment'] == segment_name]
            
            col1, col2, col3, col4 = st.columns(4)
            
            info = next((v for k, v in segment_info.items() if v['name'].startswith(segment_name.split()[0])), None)
            
            with col1:
                st.metric("Count", len(segment_data), delta=f"{(len(segment_data)/len(rfm_data)*100):.1f}%")
            
            with col2:
                st.metric("Avg Recency", f"{segment_data['Recency'].mean():.0f} days")
            
            with col3:
                st.metric("Avg Frequency", f"{segment_data['Frequency'].mean():.1f}")
            
            with col4:
                st.metric("Avg Monetary", f"£{segment_data['Monetary'].mean():.0f}")
            
            st.markdown("---")
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.box(rfm_data, x='Segment', y='Recency', color='Segment',
                        title="Recency Distribution by Segment")
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.box(rfm_data, x='Segment', y='Frequency', color='Segment',
                        title="Frequency Distribution by Segment")
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.info("""
        ### 🎯 Key Insights
        
        1. **High-Value Customers (👑)**: Focus on retention with exclusive perks
        2. **Regular Customers (🙂)**: Maintain engagement with personalized offers
        3. **Occasional Customers (😐)**: Re-engagement campaigns needed
        4. **At-Risk Customers (⚠️)**: Urgent win-back campaigns required
        
        ### 📈 Recommendations
        - Use segment-specific email campaigns
        - Tailor product recommendations per segment
        - Implement loyalty programs for high-value customers
        - Monitor at-risk customers closely
        """)

# ════════════════════════════════════════════════════════════════
# FOOTER
# ════════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #999; padding: 30px; background: white; border-radius: 10px; margin-top: 30px;'>
    <p><b>🛒 Shopper Spectrum</b> — Customer Intelligence & Product Recommendation Engine</p>
    <p>Built with ❤️ using Python, Streamlit & Machine Learning</p>
    <p style='margin-top: 15px; font-size: 0.9em;'>By Dhivya Shri S | AI & Data Science Student</p>
    <p style='margin-top: 10px;'>
        <a href='https://linkedin.com/in/dhivya-shri-153441290' style='color: #667eea; text-decoration: none;'>LinkedIn</a> • 
        <a href='https://github.com/DhivyaShri1385' style='color: #667eea; text-decoration: none;'>GitHub</a> • 
        <a href='https://dhivyashri1385.github.io' style='color: #667eea; text-decoration: none;'>Portfolio</a>
    </p>
</div>
""", unsafe_allow_html=True)