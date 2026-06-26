import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import os
from datetime import datetime

# ════════════════════════════════════════════════════════════════
# 💎 ULTRA-PREMIUM PAGE CONFIGURATION
# ════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="🛒 Shopper Spectrum | Premium Intelligence",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ════════════════════════════════════════════════════════════════
# ADVANCED PREMIUM CSS - GLASSMORPHISM + ANIMATIONS
# ════════════════════════════════════════════════════════════════
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        min-height: 100vh;
    }
    
    [data-testid="stMainBlockContainer"] {
        padding: 2rem;
    }
    
    /* GLASSMORPHISM CARDS */
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        background: rgba(255, 255, 255, 0.15);
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.5);
    }
    
    /* METRIC CARDS */
    .metric-card-premium {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.3) 0%, rgba(240, 147, 251, 0.2) 100%);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 30px;
        color: white;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .metric-card-premium::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        transform: rotate(45deg);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    .metric-card-premium:hover {
        transform: translateY(-10px);
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.4) 0%, rgba(240, 147, 251, 0.3) 100%);
        border-color: rgba(255, 255, 255, 0.3);
    }
    
    .metric-number {
        font-size: 3em;
        font-weight: 700;
        background: linear-gradient(90deg, #667eea 0%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 10px 0;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    .metric-label {
        font-size: 0.95em;
        color: rgba(255, 255, 255, 0.8);
        margin-top: 10px;
        font-weight: 500;
    }
    
    /* HEADER STYLES */
    .premium-header {
        text-align: center;
        margin: 40px 0;
        animation: fadeInDown 0.8s ease;
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .header-title {
        font-size: 4em;
        font-weight: 700;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        letter-spacing: -1px;
    }
    
    .header-subtitle {
        font-size: 1.3em;
        color: rgba(255, 255, 255, 0.7);
        margin-top: 10px;
    }
    
    /* SEGMENT CARDS */
    .segment-showcase {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        transition: all 0.3s ease;
        border-left: 5px solid;
    }
    
    .segment-showcase:hover {
        background: rgba(255, 255, 255, 0.12);
        transform: translateX(10px);
    }
    
    .segment-emoji {
        font-size: 2.5em;
        margin-bottom: 15px;
    }
    
    .segment-name {
        font-size: 1.5em;
        font-weight: 700;
        color: white;
        margin: 10px 0;
    }
    
    .segment-description {
        color: rgba(255, 255, 255, 0.7);
        font-size: 0.95em;
        margin: 10px 0;
    }
    
    /* BUTTONS */
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 15px 40px;
        font-size: 1em;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.6);
    }
    
    /* SELECTBOX & INPUT */
    .stSelectbox, .stNumberInput {
        color: white !important;
    }
    
    .stSelectbox [data-baseweb="select"] {
        background: rgba(255, 255, 255, 0.1) !important;
        border-radius: 15px !important;
    }
    
    /* TABS */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        color: white;
    }
    
    /* DIVIDERS */
    hr {
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin: 30px 0;
    }
    
    /* GRADIENTS */
    .gradient-text-1 {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .gradient-text-2 {
        background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# LOAD MODELS
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
required_files = ["kmeans_model.pkl", "rfm_scaler.pkl", "rfm_with_clusters.csv", "all_products.pkl", "product_similarity.csv"]
missing_files = [f for f in required_files if not os.path.exists(os.path.join(models_dir, f))]

if missing_files:
    st.error(f"❌ Missing: {', '.join(missing_files)}")
    st.stop()

try:
    kmeans, scaler = load_models()
    rfm_data, all_products, product_sim_df = load_data()
except Exception as e:
    st.error(f"Error: {e}")
    st.stop()

# ════════════════════════════════════════════════════════════════
# SEGMENT DATA
# ════════════════════════════════════════════════════════════════
segment_data = {
    0: {
        'name': 'Regular Customer',
        'emoji': '🙂',
        'color': '#1f77b4',
        'icon': '📊',
        'description': 'Steady purchasers with moderate spending',
        'strategy': 'Send regular newsletters and seasonal discounts',
        'stats': '45 days avg recency, 12 purchases, £800 avg spend'
    },
    1: {
        'name': 'High-Value Customer',
        'emoji': '👑',
        'color': '#2ca02c',
        'icon': '⭐',
        'description': 'Premium customers - frequent & big spenders',
        'strategy': 'Loyalty points, VIP access, exclusive offers',
        'stats': '15 days avg recency, 45 purchases, £3500+ avg spend'
    },
    2: {
        'name': 'At-Risk Customer',
        'emoji': '⚠️',
        'color': '#d62728',
        'icon': '🔔',
        'description': 'Haven\'t purchased recently',
        'strategy': 'Win-back campaigns with personalized offers',
        'stats': '250+ days avg recency, 1 purchase, £50 avg spend'
    },
    3: {
        'name': 'Occasional Customer',
        'emoji': '😐',
        'color': '#ff7f0e',
        'icon': '🎯',
        'description': 'Rare, occasional purchases',
        'strategy': 'Limited-time special offers, re-engagement',
        'stats': '180 days avg recency, 2 purchases, £150 avg spend'
    }
}

# ════════════════════════════════════════════════════════════════
# SIDEBAR
# ════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; margin: 30px 0;'>
        <div style='font-size: 3em;'>🛒</div>
        <div style='font-size: 1.5em; font-weight: bold; color: white; margin-top: 10px;'>Shopper Spectrum</div>
        <div style='color: rgba(255,255,255,0.7); font-size: 0.9em; margin-top: 5px;'>Premium Intelligence Platform</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    page = st.radio(
        "**📍 Navigation**",
        ["🎨 Dashboard", "🔮 Predictor", "🎁 Recommender", "📊 Analytics"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    st.markdown("""
    <div class='glass-card'>
        <div style='color: rgba(255,255,255,0.8); font-size: 0.9em;'>
            <p><strong>📈 Key Stats</strong></p>
            <p>👥 <strong>4,338</strong> Customers</p>
            <p>🛍️ <strong>3,877</strong> Products</p>
            <p>📊 <strong>4</strong> Segments</p>
            <p>💾 <strong>500K+</strong> Transactions</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# PAGE 1: DASHBOARD
# ════════════════════════════════════════════════════════════════
if page == "🎨 Dashboard":
    # HEADER
    st.markdown("""
    <div class='premium-header'>
        <div class='header-title'>SHOPPER SPECTRUM</div>
        <div class='header-subtitle'>Premium Customer Intelligence Platform</div>
    </div>
    """, unsafe_allow_html=True)
    
    # KEY METRICS
    col1, col2, col3, col4 = st.columns(4, gap="large")
    
    with col1:
        st.markdown(f"""
        <div class='metric-card-premium'>
            <div style='font-size: 2.5em;'>👥</div>
            <div class='metric-number'>{len(rfm_data):,}</div>
            <div class='metric-label'>Total Customers</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-card-premium'>
            <div style='font-size: 2.5em;'>🛍️</div>
            <div class='metric-number'>{3877:,}</div>
            <div class='metric-label'>Products</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='metric-card-premium'>
            <div style='font-size: 2.5em;'>📊</div>
            <div class='metric-number'>4</div>
            <div class='metric-label'>Segments</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class='metric-card-premium'>
            <div style='font-size: 2.5em;'>💾</div>
            <div class='metric-number'>500K+</div>
            <div class='metric-label'>Transactions</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # VISUALIZATIONS
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        segment_counts = rfm_data['Segment'].value_counts()
        fig_pie = go.Figure(data=[
            go.Pie(
                labels=segment_counts.index,
                values=segment_counts.values,
                hole=0.5,
                marker=dict(colors=['#2ca02c', '#1f77b4', '#d62728', '#ff7f0e']),
                textinfo="label+percent",
                hovertemplate="<b>%{label}</b><br>Customers: %{value}<br>%{percent}<extra></extra>"
            )
        ])
        fig_pie.update_layout(
            title="<b style='color: white;'>Customer Segment Distribution</b>",
            height=450,
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white', size=12),
            showlegend=True
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        segment_counts = rfm_data['Segment'].value_counts()
        fig_bar = go.Figure()
        fig_bar.add_trace(go.Bar(
            x=segment_counts.index,
            y=segment_counts.values,
            marker=dict(
                color=['#2ca02c', '#1f77b4', '#d62728', '#ff7f0e'],
                line=dict(color='white', width=2)
            ),
            text=segment_counts.values,
            textposition='outside',
            hovertemplate="<b>%{x}</b><br>Customers: %{y}<extra></extra>"
        ))
        fig_bar.update_layout(
            title="<b style='color: white;'>Segment Breakdown</b>",
            xaxis_title="<b style='color: white;'>Segment</b>",
            yaxis_title="<b style='color: white;'>Count</b>",
            height=450,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            showlegend=False
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # RFM ANALYSIS
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: white; text-align: center;'>📊 RFM Metrics Analysis</h2>", unsafe_allow_html=True)
    
    segment_stats = rfm_data.groupby('Segment')[['Recency', 'Frequency', 'Monetary']].mean()
    
    fig_rfm = make_subplots(
        rows=1, cols=3,
        subplot_titles=("Recency (Days)", "Frequency", "Monetary (£)"),
        specs=[[{"type": "bar"}, {"type": "bar"}, {"type": "bar"}]]
    )
    
    fig_rfm.add_trace(
        go.Bar(x=segment_stats.index, y=segment_stats['Recency'], name='Recency',
               marker_color='#667eea', text=segment_stats['Recency'].round(0),
               textposition='outside'),
        row=1, col=1
    )
    fig_rfm.add_trace(
        go.Bar(x=segment_stats.index, y=segment_stats['Frequency'], name='Frequency',
               marker_color='#764ba2', text=segment_stats['Frequency'].round(0),
               textposition='outside'),
        row=1, col=2
    )
    fig_rfm.add_trace(
        go.Bar(x=segment_stats.index, y=segment_stats['Monetary'], name='Monetary',
               marker_color='#f093fb', text=segment_stats['Monetary'].round(0),
               textposition='outside'),
        row=1, col=3
    )
    
    fig_rfm.update_layout(
        height=400,
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        title_text="<b style='color: white;'>RFM Metrics by Segment</b>"
    )
    
    st.plotly_chart(fig_rfm, use_container_width=True)

# ════════════════════════════════════════════════════════════════
# PAGE 2: PREDICTOR
# ════════════════════════════════════════════════════════════════
elif page == "🔮 Predictor":
    st.markdown("""
    <div class='premium-header'>
        <div class='header-title'>SEGMENT PREDICTOR</div>
        <div class='header-subtitle'>Enter Customer Metrics for Real-Time Classification</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        recency = st.number_input("📅 Days Since Last Purchase", min_value=0, max_value=1000, value=30)
    with col2:
        frequency = st.number_input("🛍️ Number of Purchases", min_value=0, max_value=500, value=5)
    with col3:
        monetary = st.number_input("💰 Total Spend (£)", min_value=0.0, max_value=100000.0, value=500.0)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🚀 PREDICT SEGMENT", use_container_width=True, type="primary"):
            input_data = np.array([[recency, frequency, monetary]])
            scaled_input = scaler.transform(input_data)
            cluster = kmeans.predict(scaled_input)[0]
            
            segment = segment_data[cluster]
            
            st.markdown(f"""
            <div style='
                background: linear-gradient(135deg, {segment["color"]}33 0%, {segment["color"]}22 100%);
                backdrop-filter: blur(10px);
                border: 2px solid {segment["color"]};
                border-radius: 25px;
                padding: 50px;
                text-align: center;
                margin: 30px 0;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            '>
                <div style='font-size: 4em; margin-bottom: 20px;'>{segment["emoji"]}</div>
                <h2 style='color: white; font-size: 2.5em; margin: 0;'>{segment["name"]}</h2>
                <p style='color: rgba(255,255,255,0.8); font-size: 1.1em; margin-top: 15px;'>{segment["description"]}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class='glass-card'>
                <h3 style='color: white;'>💡 Recommended Strategy</h3>
                <p style='color: rgba(255,255,255,0.9); font-size: 1.1em;'>{segment["strategy"]}</p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Recency", f"{recency} days")
            with col2:
                st.metric("Frequency", f"{frequency} purchases")
            with col3:
                st.metric("Monetary", f"£{monetary:.2f}")

# ════════════════════════════════════════════════════════════════
# PAGE 3: RECOMMENDER
# ════════════════════════════════════════════════════════════════
elif page == "🎁 Recommender":
    st.markdown("""
    <div class='premium-header'>
        <div class='header-title'>PRODUCT FINDER</div>
        <div class='header-subtitle'>Discover Similar Products Instantly</div>
    </div>
    """, unsafe_allow_html=True)
    
    product_input = st.selectbox(
        "🔍 **Search Products**",
        options=sorted(all_products),
        help="Type to filter"
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("✨ GET RECOMMENDATIONS", use_container_width=True, type="primary"):
            if product_input:
                product_input = product_input.upper().strip()
                
                if product_input in product_sim_df.index:
                    similar = product_sim_df[product_input].sort_values(ascending=False)[1:6]
                    
                    st.markdown("""
                    <div style='text-align: center; margin: 30px 0;'>
                        <h2 style='color: white;'>✅ Top 5 Similar Products</h2>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    for i, (product, score) in enumerate(similar.items(), 1):
                        st.markdown(f"""
                        <div class='glass-card'>
                            <div style='display: flex; justify-content: space-between; align-items: center;'>
                                <div style='flex: 1;'>
                                    <div style='font-size: 1.3em; font-weight: bold; color: white;'>
                                        #{i} {product}
                                    </div>
                                </div>
                                <div style='
                                    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
                                    color: white;
                                    padding: 12px 25px;
                                    border-radius: 15px;
                                    font-weight: bold;
                                    font-size: 1.1em;
                                '>{score*100:.1f}% Match</div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.error("❌ Product not found")

# ════════════════════════════════════════════════════════════════
# PAGE 4: ANALYTICS
# ════════════════════════════════════════════════════════════════
elif page == "📊 Analytics":
    st.markdown("""
    <div class='premium-header'>
        <div class='header-title'>ADVANCED ANALYTICS</div>
        <div class='header-subtitle'>Deep Dive into Customer Insights</div>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📌 Segment Profiles", "📈 Detailed RFM", "💼 Business Intel"])
    
    with tab1:
        st.markdown("<h3 style='color: white;'>Detailed Segment Analysis</h3>", unsafe_allow_html=True)
        
        for cluster_id, segment in segment_data.items():
            segment_df = rfm_data[rfm_data['Segment'] == segment['name']]
            
            st.markdown(f"""
            <div class='segment-showcase' style='border-left-color: {segment["color"]};'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <div>
                        <div style='font-size: 2em;'>{segment['emoji']}</div>
                        <div style='font-size: 1.4em; font-weight: bold; color: white; margin-top: 10px;'>{segment['name']}</div>
                        <div style='color: rgba(255,255,255,0.7); margin-top: 5px;'>{segment['description']}</div>
                    </div>
                    <div style='text-align: right;'>
                        <div style='font-size: 2.5em; font-weight: bold; color: {segment["color"]};'>{len(segment_df):,}</div>
                        <div style='color: rgba(255,255,255,0.7);'>Customers</div>
                        <div style='margin-top: 15px; color: rgba(255,255,255,0.7); font-size: 0.9em;'>{segment['stats']}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.box(rfm_data, x='Segment', y='Recency', color='Segment',
                        title="Recency Distribution by Segment",
                        color_discrete_map={
                            'High-Value': '#2ca02c',
                            'Regular': '#1f77b4',
                            'At-Risk': '#d62728',
                            'Occasional': '#ff7f0e'
                        })
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                            font=dict(color='white'))
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.box(rfm_data, x='Segment', y='Frequency', color='Segment',
                        title="Purchase Frequency by Segment",
                        color_discrete_map={
                            'High-Value': '#2ca02c',
                            'Regular': '#1f77b4',
                            'At-Risk': '#d62728',
                            'Occasional': '#ff7f0e'
                        })
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                            font=dict(color='white'))
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("""
        <div class='glass-card'>
            <h3 style='color: white; margin-top: 0;'>🎯 Strategic Recommendations</h3>
            
            <div style='margin-top: 20px;'>
                <h4 style='color: #2ca02c;'>👑 High-Value Customers</h4>
                <p style='color: rgba(255,255,255,0.8);'>• Implement VIP loyalty programs<br>• Exclusive early access to new products<br>• Personalized concierge service</p>
            </div>
            
            <div style='margin-top: 20px;'>
                <h4 style='color: #1f77b4;'>🙂 Regular Customers</h4>
                <p style='color: rgba(255,255,255,0.8);'>• Monthly targeted email campaigns<br>• Seasonal promotions and discounts<br>• Educational content about products</p>
            </div>
            
            <div style='margin-top: 20px;'>
                <h4 style='color: #ff7f0e;'>😐 Occasional Customers</h4>
                <p style='color: rgba(255,255,255,0.8);'>• Re-engagement campaigns<br>• Limited-time special offers<br>• Win-back incentives</p>
            </div>
            
            <div style='margin-top: 20px;'>
                <h4 style='color: #d62728;'>⚠️ At-Risk Customers</h4>
                <p style='color: rgba(255,255,255,0.8);'>• Urgent personalized outreach<br>• Crisis discounts and offers<br>• Feedback surveys to understand churn</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# FOOTER
# ════════════════════════════════════════════════════════════════
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<div style='
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    margin-top: 40px;
    color: rgba(255, 255, 255, 0.8);
'>
    <p style='margin: 0; font-size: 1.1em;'><b>🛒 Shopper Spectrum Premium</b></p>
    <p style='margin: 10px 0; opacity: 0.8;'>Customer Intelligence & Product Recommendation Engine</p>
    <p style='margin: 15px 0; font-size: 0.9em; opacity: 0.7;'>Built with ❤️ by Dhivya Shri S | AI & Data Science</p>
</div>
""", unsafe_allow_html=True)