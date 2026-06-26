# 🛒 Shopper Spectrum: Customer Segmentation & Product Recommendation

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![ML](https://img.shields.io/badge/ML-KMeans%20%7C%20Collaborative%20Filtering-green)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)

## 🔍 Problem Statement
E-commerce businesses need to understand customer behavior and recommend relevant products to maximize revenue. This project solves both challenges using machine learning.

## 🎯 What This App Does

### 1. Customer Segmentation
- Analyzes **4,338 customers** from online retail dataset
- Uses **RFM Analysis** (Recency, Frequency, Monetary)
- Applies **KMeans Clustering** to segment into 4 groups:
  - 👑 **High-Value**: Premium, frequent, recent big spenders
  - 🙂 **Regular**: Steady purchasers with moderate spending
  - 😐 **Occasional**: Rare, infrequent purchases
  - ⚠️ **At-Risk**: Haven't purchased recently

### 2. Product Recommendations
- Analyzes **3,877 unique products**
- Uses **Item-based Collaborative Filtering**
- Computes **Cosine Similarity** between products
- Recommends **5 similar products** for any item

## 📊 Dataset
- **Source**: Online Retail Dataset
- **Records**: 500K+ transactions
- **Products**: 3,877 unique items
- **Customers**: 4,338 unique customers
- **Period**: 2022-2023

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.12** | Core language |
| **Pandas & NumPy** | Data processing |
| **Scikit-learn** | Machine learning models |
| **Streamlit** | Interactive web application |
| **Matplotlib & Seaborn** | Data visualizations |
| **Plotly** | Interactive charts |
| **Jupyter** | Exploratory analysis |

## 🚀 How to Run

### 1. Clone Repository
```bash
git clone https://github.com/DhivyaShri1385/Shopper-Spectrum-Ecommerce.git
cd Shopper-Spectrum-Ecommerce
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate Models (First Time Only)
Run all cells in `notebooks/shopper_spectrum.ipynb` to generate model files

### 4. Run Streamlit App
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📁 Project Structure 

shopper-spectrum-ecommerce/

├── notebooks/

│   └── shopper_spectrum.ipynb      # Complete ML pipeline

├── data/

│   └── online_retail.csv           # Raw dataset

├── models/                         # Generated models (git ignored)

│   ├── kmeans_model.pkl

│   ├── rfm_scaler.pkl

│   ├── rfm_with_clusters.csv

│   └── product_similarity.csv

├── assets/                         # EDA visualizations

│   ├── eda_countries.png

│   ├── eda_products.png

│   ├── rfm_distributions.png

│   └── elbow_silhouette.png

├── app.py                          # Streamlit application

├── requirements.txt

└── README.md

## 📈 Key Results

### Customer Segmentation
- **Silhouette Score**: ~0.45 (optimal clustering)
- **4 Distinct Segments** identified with clear RFM patterns
- **Actionable insights** for targeted marketing

### Product Recommendations
- **3,877 products** analyzed
- **Item-based collaborative filtering** using cosine similarity
- Real-time recommendations based on purchase patterns

## 🎓 Machine Learning Pipeline

### Block 1: Data Loading
- Load 500K+ transactions
- Explore data types and structure

### Block 2: Data Preprocessing
- Remove cancelled invoices
- Handle missing values
- Remove invalid transactions (negative/zero amounts)

### Block 3: Exploratory Data Analysis
- Visualize top countries and products
- Analyze revenue trends
- Examine transaction distributions

### Block 4: RFM Feature Engineering
- Calculate Recency, Frequency, Monetary metrics
- Standardize features using StandardScaler
- Create customer behavior profiles

### Block 5: Clustering
- Use Elbow Method to find optimal k
- Calculate Silhouette Scores
- Train KMeans with k=4
- Label clusters based on RFM characteristics
- Save models for production

### Block 6: Recommendation System
- Build customer-product purchase matrix
- Compute cosine similarity between products
- Implement recommendation function
- Save similarity matrix for app

## 🎯 Streamlit App Features

### 🏠 Home Page
- Project overview
- Key statistics (customers, algorithm, method)
- Segment distribution visualization

### 🔍 Customer Segmentation Page
- Input customer RFM metrics
- Real-time segment prediction
- Marketing strategy recommendations
- Segment benchmarks comparison

### 🎯 Product Recommendation Page
- Search any product
- Get top 5 similar products
- View similarity scores
- Support for 3,877 products

## 💡 Business Use Cases

1. **Targeted Marketing**: Send different campaigns to each segment
2. **Personalized Recommendations**: Increase average order value
3. **Customer Retention**: Identify and re-engage at-risk customers
4. **Inventory Management**: Stock products based on segment demand
5. **Dynamic Pricing**: Adjust prices by customer segment

## 📊 Sample Results

### Segment Characteristics (Averages)
| Segment | Recency (days) | Frequency | Monetary (£) |
|---------|----------------|-----------|-------------|
| High-Value | 15 | 45 | £3,500+ |
| Regular | 45 | 12 | £800 |
| Occasional | 180 | 2 | £150 |
| At-Risk | 250+ | 1 | £50 |

### Top Products
1. WHITE HANGING HEART T-LIGHT HOLDER - 12,000+ units
2. REGENCY TEA CUP AND SAUCER - 10,500+ units
3. JUMBO BAG RED RETROSPOT - 9,500+ units

## 🔐 Model Persistence

- **KMeans Model**: `models/kmeans_model.pkl`
- **Scaler**: `models/rfm_scaler.pkl`
- **RFM Data**: `models/rfm_with_clusters.csv`
- **Product Similarity**: `models/product_similarity.csv` (git ignored, ~300MB)

## ⚠️ Important Notes

- Large model files (>100MB) are in `.gitignore` and won't be committed to GitHub
- Run the Jupyter notebook first to generate these files locally
- The Streamlit app requires these generated files to function

## 👩‍💻 Author

**Dhivya Shri S**
- B.Tech AI & Data Science (2023-2027)
- M. Kumarasamy College of Engineering, Tamil Nadu
- 2x Internship Experience | IEEE Published Researcher

### Socials
- 🔗 [LinkedIn](https://linkedin.com/in/dhivya-shri-153441290)
- 💻 [GitHub](https://github.com/DhivyaShri1385)
- 🌐 [Portfolio](https://dhivyashri1385.github.io)

## 📝 Certifications
- ✅ Fortinet Certified Associate Cybersecurity
- ✅ NPTEL Ethical Hacking (Elite)
- ✅ TryHackMe NetSEC Room (Ranked #1)
- ✅ Tata IAM Job Simulation
- ✅ Deloitte Data Analytics Job Simulation

## 📄 License
This project is open source and available under the MIT License.

---

**Last Updated**: June 2026
**Status**: ✅ Complete & Production Ready