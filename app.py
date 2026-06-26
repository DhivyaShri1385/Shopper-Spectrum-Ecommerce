import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(
    page_title="🛒 Shopper Spectrum",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Shopper Spectrum")
st.subheader("Customer Segmentation & Product Recommendation System")

# Check if model files exist
models_dir = "models"
required_files = [
    "kmeans_model.pkl",
    "rfm_scaler.pkl",
    "rfm_with_clusters.csv",
    "all_products.pkl",
    "product_similarity.csv"
]

missing_files = [f for f in required_files if not os.path.exists(os.path.join(models_dir, f))]

if missing_files:
    st.error(f"""
    ❌ Missing model files: {', '.join(missing_files)}
    
    Please run the Jupyter notebook blocks first to generate these files:
    1. Block 5 (Clustering) - generates kmeans_model.pkl, rfm_scaler.pkl, rfm_with_clusters.csv
    2. Block 6 (Recommendations) - generates product_similarity.csv, all_products.pkl
    """)
    st.stop()

# Load models
try:
    kmeans = joblib.load(os.path.join(models_dir, "kmeans_model.pkl"))
    scaler = joblib.load(os.path.join(models_dir, "rfm_scaler.pkl"))
    rfm_data = pd.read_csv(os.path.join(models_dir, "rfm_with_clusters.csv"))
    all_products = joblib.load(os.path.join(models_dir, "all_products.pkl"))
    product_sim_df = pd.read_csv(os.path.join(models_dir, "product_similarity.csv"), index_col=0)
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

# Sidebar
st.sidebar.title("🛒 Shopper Spectrum")
page = st.sidebar.radio("Navigate", ["🏠 Home", "🔍 Customer Segmentation", "🎯 Product Recommendation"])

cluster_labels = {
    0: ('Regular Customer 🙂', '#1f77b4'),
    1: ('High-Value Customer 👑', '#2ca02c'),
    2: ('At-Risk Customer ⚠️', '#d62728'),
    3: ('Occasional Customer 😐', '#ff7f0e')
}

marketing_tips = {
    0: "📧 Send regular newsletters and moderate seasonal discounts",
    1: "🎁 Reward with loyalty points, VIP access, and exclusive offers",
    2: "🚨 Send win-back campaigns with personalized offers urgently",
    3: "🎯 Re-engage with limited-time special offers"
}

# PAGE 1: HOME
if page == "🏠 Home":
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", f"{len(rfm_data):,}")
    col2.metric("Algorithm", "KMeans")
    col3.metric("Recommendation", "Cosine Similarity")
    
    st.markdown("---")
    st.write("""
    ### 🎯 What This App Does
    
    **1. Customer Segmentation** - Analyzes RFM metrics and segments customers
    **2. Product Recommendations** - Suggests similar products using collaborative filtering
    """)

# PAGE 2: CUSTOMER SEGMENTATION
elif page == "🔍 Customer Segmentation":
    st.title("🔍 Customer Segmentation")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        recency = st.number_input("Recency (days)", min_value=0, max_value=1000, value=30)
    with col2:
        frequency = st.number_input("Frequency (purchases)", min_value=0, max_value=500, value=5)
    with col3:
        monetary = st.number_input("Monetary (£)", min_value=0.0, max_value=100000.0, value=500.0)
    
    if st.button("🔮 Predict Segment", use_container_width=True):
        input_data = np.array([[recency, frequency, monetary]])
        scaled_input = scaler.transform(input_data)
        cluster = kmeans.predict(scaled_input)[0]
        
        segment_name, color = cluster_labels[cluster]
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color} 0%, {color}cc 100%);
                    padding: 30px; border-radius: 10px; text-align: center;
                    margin: 20px 0; color: white;'>
            <h2 style='margin: 0;'>{segment_name}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.info(f"💡 **Strategy**: {marketing_tips[cluster]}")

# PAGE 3: PRODUCT RECOMMENDATION
elif page == "🎯 Product Recommendation":
    st.title("🎯 Product Recommendation")
    
    product_input = st.selectbox("Search for a product", options=sorted(all_products))
    
    if st.button("🔍 Get Recommendations", use_container_width=True):
        if product_input:
            product_input = product_input.upper().strip()
            
            if product_input in product_sim_df.index:
                similar = product_sim_df[product_input].sort_values(ascending=False)[1:6]
                
                st.success("✅ Top 5 Similar Products:")
                for i, (product, score) in enumerate(similar.items(), 1):
                    st.markdown(f"**{i}. {product}** (similarity: {score:.2%})")
            else:
                st.error("Product not found")

st.markdown("---")
