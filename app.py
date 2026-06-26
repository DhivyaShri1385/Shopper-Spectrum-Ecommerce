import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="Analytics Pro", page_icon="📊", layout="wide", initial_sidebar_state="expanded")

st.markdown("""<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    * {font-family: 'Inter', sans-serif; letter-spacing: -0.4px;}
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0a0a0a 0%, #050505 50%, #0a0a0a 100%), 
        radial-gradient(circle at 20% 35%, rgba(0, 255, 179, 0.04) 0%, transparent 25%),
        radial-gradient(circle at 85% 70%, rgba(163, 255, 18, 0.03) 0%, transparent 25%);
        background-attachment: fixed;
        min-height: 100vh;
    }
    [data-testid="stMainBlockContainer"] {padding: 0 20px 20px 20px; background: transparent;}
    [data-testid="stSidebar"] {background: rgba(8, 8, 18, 0.85) !important; border-right: 1px solid rgba(163, 255, 18, 0.12); backdrop-filter: blur(20px) !important;}
    
    .metric-card {
        background: rgba(8, 8, 18, 0.5);
        border: 1px solid rgba(163, 255, 18, 0.16);
        border-radius: 14px;
        padding: 14px;
        backdrop-filter: blur(30px);
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.4), 0 0 1px rgba(163, 255, 18, 0.15) inset;
        transition: all 0.3s ease;
    }
    .metric-card:hover {border-color: rgba(163, 255, 18, 0.3); background: rgba(8, 8, 18, 0.6); box-shadow: 0 0 40px rgba(163, 255, 18, 0.2);}
    .metric-value {font-size: 1.8em; font-weight: 700; background: linear-gradient(135deg, #A3FF12, #00FFB3); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 4px 0;}
    .metric-label {font-size: 0.7em; color: rgba(255, 255, 255, 0.6); font-weight: 500; text-transform: uppercase;}
    .metric-change {font-size: 0.7em; color: #A3FF12; font-weight: 600; margin-top: 3px;}
    
    h1 {font-size: 1.8em; background: linear-gradient(135deg, #A3FF12, #00FFB3); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0;}
    h2 {font-size: 15px; color: white; margin: 10px 0 8px 0; border-bottom: 1px solid rgba(163, 255, 18, 0.1); padding-bottom: 6px; font-weight: 600;}
    p {color: rgba(255, 255, 255, 0.7); margin: 0;}
    hr {border: none; height: 1px; background: linear-gradient(90deg, transparent, rgba(163, 255, 18, 0.15), transparent); margin: 10px 0;}
</style>""", unsafe_allow_html=True)

@st.cache_data
def get_data():
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', '2024-12-31', freq='D')
    revenue = np.cumsum(np.random.normal(1000, 500, len(dates))) + 50000
    customers = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Carol', 'David', 'Emma'],
        'Email': ['a@ex.com', 'b@ex.com', 'c@ex.com', 'd@ex.com', 'e@ex.com'],
        'Status': ['Active', 'Active', 'Inactive', 'Active', 'Pending'],
        'MRR': [5200, 3800, 2100, 7500, 4300]
    })
    return dates, revenue, customers

dates, revenue, customers = get_data()

with st.sidebar:
    st.markdown("<div style='text-align:center;padding:16px 0;border-bottom:1px solid rgba(163,255,18,0.1);'><div style='font-size:1.8em;margin-bottom:6px;'>📊</div><div style='font-size:1.2em;font-weight:800;background:linear-gradient(135deg,#A3FF12,#00FFB3);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>PRO</div><div style='color:rgba(255,255,255,0.5);font-size:0.75em;'>Premium</div></div>", unsafe_allow_html=True)
    st.markdown("<div style='padding:10px 0;'></div>", unsafe_allow_html=True)
    page = st.radio("Nav", ["📊 Dashboard", "📈 Analytics", "💰 Revenue", "👥 Customers"], label_visibility="collapsed")

if page == "📊 Dashboard":
    st.markdown("<div style='padding:16px 0;border-bottom:1px solid rgba(163,255,18,0.1);margin-bottom:12px;'><h1>Dashboard</h1><p style='font-size:0.85em;margin-top:2px;'>Performance</p></div>", unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4, gap="small")
    for col, (emoji, label, value, change) in zip([c1, c2, c3, c4], [("💰", "Revenue", "$487.5K", "↑23.5%"), ("📊", "ARR", "$5.8M", "↑18.2%"), ("🎯", "Conv", "4.23%", "↑1.2%"), ("👥", "Users", "12.8K", "↑8.7%")]):
        with col:
            st.markdown(f"<div class='metric-card'><div style='font-size:1.4em;'>{emoji}</div><div class='metric-label'>{label}</div><div class='metric-value'>{value}</div><div class='metric-change'>{change}</div></div>", unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown("<h2>💹 Revenue</h2>", unsafe_allow_html=True)
        fig = go.Figure(data=[go.Scatter(x=dates, y=revenue, fill='tozeroy', fillcolor='rgba(163,255,18,0.1)', line=dict(color='#A3FF12', width=2))])
        fig.update_layout(height=320, margin=dict(t=0,b=0,l=30,r=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(size=11), showlegend=False, xaxis=dict(tickfont=dict(size=10)), yaxis=dict(tickfont=dict(size=10)))
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    with c2:
        st.markdown("<h2>🍰 Sources</h2>", unsafe_allow_html=True)
        fig = go.Figure(data=[go.Pie(labels=['Organic', 'Paid', 'Referral', 'Direct'], values=[4500, 2800, 1200, 1500], hole=0.4, marker=dict(colors=['#A3FF12', '#00FFB3', '#00D9FF', '#A78BFA']))])
        fig.update_layout(height=200, margin=dict(t=0,b=0,l=0,r=0), paper_bgcolor='rgba(0,0,0,0)', font=dict(size=11), showlegend=True)
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown("<h2>📊 DAU</h2>", unsafe_allow_html=True)
        dau = np.cumsum(np.random.normal(100, 50, len(dates))) + 5000
        fig = go.Figure(data=[go.Bar(x=dates, y=dau, marker=dict(color='rgba(0,255,179,0.6)'))])
        fig.update_layout(height=320, margin=dict(t=0,b=0,l=30,r=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(size=11), showlegend=False, xaxis=dict(tickfont=dict(size=10)), yaxis=dict(tickfont=dict(size=10)))
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    with c2:
        st.markdown("<h2>🔥 Top</h2>", unsafe_allow_html=True)
        fig = go.Figure(data=[go.Bar(x=[4200,3800,2100,1500], y=['A','B','C','D'], orientation='h', marker=dict(color='#A3FF12'))])
        fig.update_layout(height=320, margin=dict(t=0,b=0,l=30,r=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(size=11), showlegend=False, xaxis=dict(tickfont=dict(size=10)), yaxis=dict(tickfont=dict(size=10)))
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h2>👥 Customers</h2>", unsafe_allow_html=True)
    st.dataframe(customers, use_container_width=True, hide_index=True)

elif page == "📈 Analytics":
    st.markdown("<div style='padding:16px 0;border-bottom:1px solid rgba(163,255,18,0.1);margin-bottom:12px;'><h1>Analytics</h1></div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<h2>📈 Growth</h2>", unsafe_allow_html=True)
        for m, v in [("Weekly","+12.5%"), ("Monthly","+28.3%"), ("Quarterly","+45.8%"), ("YoY","+156.2%")]:
            st.markdown(f"<div style='padding:8px;border-left:3px solid #A3FF12;margin:4px 0;'><strong>{m}</strong> <span style='color:#A3FF12;'>{v}</span></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<h2>🎯 Funnel</h2>", unsafe_allow_html=True)
        fig = go.Figure(go.Funnel(y=['Visitors','Signups','Trials','Customers'], x=[50000,8500,3200,487], marker=dict(color=['#A3FF12','#00FFB3','#00D9FF','#A78BFA'])))
        fig.update_layout(height=230, margin=dict(t=0,b=0,l=60,r=10), paper_bgcolor='rgba(0,0,0,0)', font=dict(size=11), yaxis=dict(tickfont=dict(size=10)))
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

elif page == "💰 Revenue":
    st.markdown("<div style='padding:16px 0;border-bottom:1px solid rgba(163,255,18,0.1);margin-bottom:12px;'><h1>Revenue</h1></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3, gap="small")
    for col, (emoji, label, value, change) in zip([c1, c2, c3], [("💵", "MRR", "$487.5K", "↑15%"), ("📈", "ARR", "$5.8M", "↑28%"), ("💳", "LTV", "$12.5K", "↑8%")]):
        with col:
            st.markdown(f"<div class='metric-card'><div style='font-size:1.4em;'>{emoji}</div><div class='metric-label'>{label}</div><div class='metric-value'>{value}</div><div class='metric-change'>{change}</div></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h2>📊 By Plan</h2>", unsafe_allow_html=True)
    fig = go.Figure(data=[go.Bar(x=['Starter','Pro','Enterprise'], y=[1200000,2800000,1800000], marker=dict(color=['#A3FF12','#00FFB3','#00D9FF']))])
    fig.update_layout(height=320, margin=dict(t=0,b=0,l=30,r=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(size=11), showlegend=False, xaxis=dict(tickfont=dict(size=10)), yaxis=dict(tickfont=dict(size=10)))
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

elif page == "👥 Customers":
    st.markdown("<div style='padding:16px 0;border-bottom:1px solid rgba(163,255,18,0.1);margin-bottom:12px;'><h1>Customers</h1></div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2, gap="small")
    with c1:
        st.markdown("<div class='metric-card'><div style='font-size:1.4em;'>👥</div><div class='metric-label'>Total</div><div class='metric-value'>1,247</div><div class='metric-change'>↑23%</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='metric-card'><div style='font-size:1.4em;'>⭐</div><div class='metric-label'>Rating</div><div class='metric-value'>4.8/5</div><div class='metric-change'>↑0.2</div></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h2>👥 All</h2>", unsafe_allow_html=True)
    st.dataframe(customers, use_container_width=True, hide_index=True)