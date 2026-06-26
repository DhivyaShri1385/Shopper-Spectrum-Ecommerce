# 🛒 Shopper Spectrum: Customer Segmentation & Product Recommendation

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![ML](https://img.shields.io/badge/ML-KMeans%20%7C%20Collaborative%20Filtering-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 🔍 Problem Statement
E-commerce businesses struggle to understand customer behavior and recommend 
relevant products. This project solves both problems using machine learning.

## 🎯 What This App Does
- Segments customers into **High-Value, Regular, Occasional, At-Risk** groups
- Recommends **5 similar products** based on purchase history
- Built on **RFM Analysis + KMeans Clustering + Cosine Similarity**

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas & NumPy | Data processing |
| Scikit-learn | ML models |
| Streamlit | Web app |
| Matplotlib & Seaborn | Visualizations |

## 📊 Dataset
- Source: Online Retail Dataset (UCI / Kaggle)
- Records: ~500K transactions
- Period: 2022–2023

## 🚀 How to Run
```bash
git clone https://github.com/DhivyaShri1385/shopper-spectrum-ecommerce.git
cd shopper-spectrum-ecommerce
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Project Structure

├── data/                  # Dataset

├── notebooks/             # Jupyter notebook with EDA & modeling

├── models/                # Saved ML models

├── assets/                # EDA visualizations

├── app.py                 # Streamlit application

└── requirements.txt

## 📌 Key Results
- Customer segments identified with Silhouette Score evaluation
- Product recommendations using Item-based Collaborative Filtering
- Interactive Streamlit app with real-time predictions

## 👩‍💻 Author
**Dhivya Shri S** — AI & Data Science Undergraduate
- LinkedIn: [linkedin.com/in/dhivya-shri-153441290](https://linkedin.com/in/dhivya-shri-153441290)
- GitHub: [github.com/DhivyaShri1385](https://github.com/DhivyaShri1385)
- Portfolio: [dhivyashri1385.github.io](https://dhivyashri1385.github.io)