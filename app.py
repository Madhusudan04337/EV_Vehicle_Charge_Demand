import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime
import matplotlib.pyplot as plt

# Set Streamlit page config first thing
st.set_page_config(page_title="EV Forecast", layout="wide")

# === Load model ===
model = joblib.load('forecasting_ev_model.pkl')

# === Futuristic Electric-Themed Styling ===
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;500;600;700&display=swap');
        
        .stApp {
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #533483 100%);
            color: #ffffff;
        }
        
        /* Animated background particles */
        .stApp::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                radial-gradient(2px 2px at 20px 30px, #00ffff, transparent),
                radial-gradient(2px 2px at 40px 70px, #ff00ff, transparent),
                radial-gradient(1px 1px at 90px 40px, #ffff00, transparent),
                radial-gradient(1px 1px at 130px 80px, #00ff00, transparent);
            background-repeat: repeat;
            background-size: 200px 100px;
            animation: sparkle 20s linear infinite;
            opacity: 0.1;
            pointer-events: none;
            z-index: 0;
        }
        
        @keyframes sparkle {
            0% { transform: translateY(0px); }
            100% { transform: translateY(-100px); }
        }
        
        .main-container {
            position: relative;
            z-index: 1;
        }
        
        .hero-section {
            background: linear-gradient(135deg, rgba(0,255,255,0.1) 0%, rgba(255,0,255,0.1) 100%);
            border: 2px solid transparent;
            background-clip: padding-box;
            border-radius: 25px;
            padding: 3rem 2rem;
            margin: 2rem 0;
            text-align: center;
            position: relative;
            overflow: hidden;
            box-shadow: 
                0 0 50px rgba(0,255,255,0.3),
                inset 0 0 50px rgba(255,0,255,0.1);
        }
        
        .hero-section::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: linear-gradient(45deg, #00ffff, #ff00ff, #ffff00, #00ff00);
            border-radius: 25px;
            z-index: -1;
            animation: borderGlow 3s ease-in-out infinite alternate;
        }
        
        @keyframes borderGlow {
            0% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        
        .electric-title {
            font-family: 'Orbitron', monospace;
            font-size: 3.5rem;
            font-weight: 900;
            background: linear-gradient(45deg, #00ffff, #ff00ff, #ffff00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1rem;
            text-shadow: 0 0 30px rgba(0,255,255,0.5);
            animation: titlePulse 2s ease-in-out infinite alternate;
        }
        
        @keyframes titlePulse {
            0% { transform: scale(1); }
            100% { transform: scale(1.02); }
        }
        
        .electric-subtitle {
            font-family: 'Exo 2', sans-serif;
            font-size: 1.4rem;
            color: #00ffff;
            margin-bottom: 1rem;
            text-shadow: 0 0 20px rgba(0,255,255,0.7);
        }
        
        .electric-description {
            font-family: 'Exo 2', sans-serif;
            font-size: 1.1rem;
            color: #e0e0e0;
            margin: 0 auto;
            text-align: center;
            line-height: 1.6;
        }
        
        .tech-card {
            background: linear-gradient(135deg, rgba(0,255,255,0.05) 0%, rgba(255,0,255,0.05) 100%);
            border: 1px solid rgba(0,255,255,0.3);
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            backdrop-filter: blur(10px);
            box-shadow: 
                0 8px 32px rgba(0,0,0,0.3),
                0 0 20px rgba(0,255,255,0.1);
            position: relative;
            overflow: hidden;
        }
        
        .tech-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(0,255,255,0.1), transparent);
            animation: shimmer 3s infinite;
        }
        
        @keyframes shimmer {
            0% { left: -100%; }
            100% { left: 100%; }
        }
        
        .section-title {
            font-family: 'Orbitron', monospace;
            font-size: 1.8rem;
            font-weight: 700;
            color: #00ffff;
            margin-bottom: 1rem;
            text-shadow: 0 0 15px rgba(0,255,255,0.7);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .data-display {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            border: 2px solid #00ffff;
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            text-align: center;
            box-shadow: 
                0 0 30px rgba(0,255,255,0.4),
                inset 0 0 20px rgba(0,255,255,0.1);
            animation: dataGlow 2s ease-in-out infinite alternate;
        }
        
        @keyframes dataGlow {
            0% { box-shadow: 0 0 30px rgba(0,255,255,0.4), inset 0 0 20px rgba(0,255,255,0.1); }
            100% { box-shadow: 0 0 40px rgba(0,255,255,0.6), inset 0 0 30px rgba(0,255,255,0.2); }
        }
        
        .metric-value {
            font-family: 'Orbitron', monospace;
            font-size: 2rem;
            font-weight: 700;
            color: #ffff00;
            text-shadow: 0 0 20px rgba(255,255,0,0.7);
        }
        
        .comparison-zone {
            background: linear-gradient(135deg, rgba(255,0,255,0.05) 0%, rgba(255,255,0,0.05) 100%);
            border: 1px solid rgba(255,0,255,0.3);
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            backdrop-filter: blur(10px);
        }
        
        .neural-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }
        
        .neural-cell {
            background: linear-gradient(135deg, rgba(0,255,0,0.1) 0%, rgba(0,255,255,0.1) 100%);
            border: 1px solid rgba(0,255,0,0.4);
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.3s ease;
        }
        
        .neural-cell:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,255,0,0.3);
            border-color: rgba(0,255,0,0.8);
        }
        
        .footer-tech {
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 100%);
            border: 1px solid rgba(0,255,255,0.3);
            border-radius: 15px;
            padding: 2rem;
            margin-top: 3rem;
            text-align: center;
            font-family: 'Exo 2', sans-serif;
        }
        
        /* Enhanced Streamlit component styling */
        .stSelectbox > div > div {
            background: linear-gradient(135deg, rgba(0,255,255,0.1) 0%, rgba(255,0,255,0.1) 100%);
            border: 2px solid rgba(0,255,255,0.5);
            border-radius: 10px;
            color: #ffffff;
        }
        
        .stMultiSelect > div > div {
            background: linear-gradient(135deg, rgba(0,255,255,0.1) 0%, rgba(255,0,255,0.1) 100%);
            border: 2px solid rgba(0,255,255,0.5);
            border-radius: 10px;
            color: #ffffff;
        }
        
        .stSuccess {
            background: linear-gradient(135deg, rgba(0,255,0,0.2) 0%, rgba(0,255,255,0.2) 100%);
            border: 1px solid rgba(0,255,0,0.5);
            border-radius: 10px;
            color: #00ff00;
            box-shadow: 0 0 20px rgba(0,255,0,0.3);
        }
        
        .stWarning {
            background: linear-gradient(135deg, rgba(255,255,0,0.2) 0%, rgba(255,0,255,0.2) 100%);
            border: 1px solid rgba(255,255,0,0.5);
            border-radius: 10px;
            color: #ffff00;
            box-shadow: 0 0 20px rgba(255,255,0,0.3);
        }
        
        /* Image styling */
        .stImage > img {
            border-radius: 15px;
            box-shadow: 0 0 30px rgba(0,255,255,0.3);
            border: 2px solid rgba(0,255,255,0.2);
        }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class='hero-section'>
        <h1 class='electric-title'>⚡ EV NEXUS FORECASTER</h1>
        <p class='electric-subtitle'>🚗 Advanced Neural Prediction System</p>
        <p class='electric-description'>
            Harness the power of quantum-enhanced machine learning algorithms to predict 
            electric vehicle adoption patterns across Washington State counties. 
            Experience the future of transportation analytics.
        </p>
    </div>
""", unsafe_allow_html=True)

# Enhanced image with electric border
st.image("ev-car-factory.png", use_container_width=True)

# === Load data (must contain historical values, features, etc.) ===
@st.cache_data
def load_data():
    df = pd.read_csv("preprocessed_ev_data.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# County Selection with Tech Styling
st.markdown("""
    <div class='tech-card'>
        <h2 class='section-title'>🎯 NEURAL COUNTY SELECTOR</h2>
        <p style='color: #e0e0e0; margin-bottom: 1.5rem;'>
            Initialize quantum analysis by selecting your target county for deep EV pattern recognition.
        </p>
    </div>
""", unsafe_allow_html=True)

county_list = sorted(df['County'].dropna().unique().tolist())
county = st.selectbox("🔍 SELECT COUNTY FOR ANALYSIS", county_list, key="county_select")

if county not in df['County'].unique():
    st.warning(f"⚠️ County '{county}' not found in neural database.")
    st.stop()

county_df = df[df['County'] == county].sort_values("Date")
county_code = county_df['county_encoded'].iloc[0]

# === Forecasting ===
historical_ev = list(county_df['Electric Vehicle (EV) Total'].values[-6:])
cumulative_ev = list(np.cumsum(historical_ev))
months_since_start = county_df['months_since_start'].max()
latest_date = county_df['Date'].max()

future_rows = []
forecast_horizon = 36

for i in range(1, forecast_horizon + 1):
    forecast_date = latest_date + pd.DateOffset(months=i)
    months_since_start += 1
    
    lag1, lag2, lag3 = historical_ev[-1], historical_ev[-2], historical_ev[-3]
    roll_mean = np.mean([lag1, lag2, lag3])
    pct_change_1 = (lag1 - lag2) / lag2 if lag2 != 0 else 0
    pct_change_3 = (lag1 - lag3) / lag3 if lag3 != 0 else 0
    
    recent_cumulative = cumulative_ev[-6:]
    ev_growth_slope = np.polyfit(range(len(recent_cumulative)), recent_cumulative, 1)[0] if len(recent_cumulative) == 6 else 0
    
    new_row = {
        'months_since_start': months_since_start,
        'county_encoded': county_code,
        'ev_total_lag1': lag1,
        'ev_total_lag2': lag2,
        'ev_total_lag3': lag3,
        'ev_total_roll_mean_3': roll_mean,
        'ev_total_pct_change_1': pct_change_1,
        'ev_total_pct_change_3': pct_change_3,
        'ev_growth_slope': ev_growth_slope
    }
    
    pred = model.predict(pd.DataFrame([new_row]))[0]
    future_rows.append({"Date": forecast_date, "Predicted EV Total": round(pred)})
    
    historical_ev.append(pred)
    if len(historical_ev) > 6:
        historical_ev.pop(0)
    
    cumulative_ev.append(cumulative_ev[-1] + pred)
    if len(cumulative_ev) > 6:
        cumulative_ev.pop(0)

# === Combine Historical + Forecast for Cumulative Plot ===
historical_cum = county_df[['Date', 'Electric Vehicle (EV) Total']].copy()
historical_cum['Source'] = 'Historical'
historical_cum['Cumulative EV'] = historical_cum['Electric Vehicle (EV) Total'].cumsum()

forecast_df = pd.DataFrame(future_rows)
forecast_df['Source'] = 'Forecast'
forecast_df['Cumulative EV'] = forecast_df['Predicted EV Total'].cumsum() + historical_cum['Cumulative EV'].iloc[-1]

combined = pd.concat([
    historical_cum[['Date', 'Cumulative EV', 'Source']],
    forecast_df[['Date', 'Cumulative EV', 'Source']]
], ignore_index=True)

# === Enhanced Futuristic Plot ===
st.markdown(f"""
    <div class='tech-card'>
        <h2 class='section-title'>📊 QUANTUM FORECAST VISUALIZATION</h2>
        <p style='color: #e0e0e0; margin-bottom: 1.5rem;'>
            Neural network predictions for {county} County - 36-month projection matrix
        </p>
    </div>
""", unsafe_allow_html=True)

# Create futuristic plot
fig, ax = plt.subplots(figsize=(14, 8))
fig.patch.set_facecolor('#0f0f23')
ax.set_facecolor('#1a1a2e')

# Electric colors for the plot
electric_colors = ['#00ffff', '#ff00ff']
for i, (label, data) in enumerate(combined.groupby('Source')):
    ax.plot(data['Date'], data['Cumulative EV'], 
           label=label, marker='o', linewidth=3, 
           markersize=7, color=electric_colors[i], 
           markerfacecolor=electric_colors[i],
           markeredgecolor='white', markeredgewidth=1,
           alpha=0.9)

ax.set_title(f"⚡ NEURAL EV PREDICTION MATRIX - {county} COUNTY ⚡", 
            fontsize=18, color='#00ffff', fontweight='bold', pad=25,
            fontfamily='monospace')
ax.set_xlabel("TEMPORAL AXIS", color='#00ffff', fontsize=14, fontfamily='monospace')
ax.set_ylabel("CUMULATIVE EV UNITS", color='#00ffff', fontsize=14, fontfamily='monospace')

# Electric grid
ax.grid(True, alpha=0.3, color='#00ffff', linestyle='--')
ax.tick_params(colors='#ffffff', labelsize=11)

# Futuristic legend
legend = ax.legend(fontsize=12, framealpha=0.8, 
                  facecolor='#1a1a2e', edgecolor='#00ffff',
                  title="DATA STREAMS", title_fontsize=13)
legend.get_frame().set_facecolor('#1a1a2e')
legend.get_title().set_color('#00ffff')
for text in legend.get_texts():
    text.set_color('#ffffff')

plt.tight_layout()
st.pyplot(fig)

# === Futuristic Results Display ===
historical_total = historical_cum['Cumulative EV'].iloc[-1]
forecasted_total = forecast_df['Cumulative EV'].iloc[-1]

if historical_total > 0:
    forecast_growth_pct = ((forecasted_total - historical_total) / historical_total) * 100
    trend = "SURGE ⚡" if forecast_growth_pct > 0 else "DECLINE ⚡"
    
    st.markdown(f"""
        <div class='data-display'>
            <h3 style='color: #00ffff; margin: 0 0 15px 0; font-family: Orbitron;'>🎯 NEURAL ANALYSIS COMPLETE</h3>
            <div class='metric-value'>{forecast_growth_pct:.2f}%</div>
            <p style='font-size: 1.2rem; margin: 10px 0 0 0; color: #e0e0e0;'>
                EV adoption in <span style='color: #00ffff;'>{county}</span> shows projected {trend} over 36 months
            </p>
        </div>
    """, unsafe_allow_html=True)
else:
    st.warning("⚠️ Insufficient historical data for quantum analysis.")

# === Multi-County Comparison Zone ===
st.markdown("""
    <div class='comparison-zone'>
        <h2 class='section-title' style='color: #ff00ff;'>🔄 MULTI-DIMENSIONAL ANALYSIS</h2>
        <p style='color: #e0e0e0; margin-bottom: 1.5rem;'>
            Activate parallel universe comparison - analyze up to 3 counties simultaneously
        </p>
    </div>
""", unsafe_allow_html=True)

multi_counties = st.multiselect("🌐 SELECT COUNTIES FOR PARALLEL ANALYSIS", county_list, max_selections=3)
if multi_counties:
    comparison_data = []
    
    for cty in multi_counties:
        cty_df = df[df['County'] == cty].sort_values("Date")
        cty_code = cty_df['county_encoded'].iloc[0]
        
        hist_ev = list(cty_df['Electric Vehicle (EV) Total'].values[-6:])
        cum_ev = list(np.cumsum(hist_ev))
        months_since = cty_df['months_since_start'].max()
        last_date = cty_df['Date'].max()
        
        future_rows_cty = []
        
        for i in range(1, forecast_horizon + 1):
            forecast_date = last_date + pd.DateOffset(months=i)
            months_since += 1
            
            lag1, lag2, lag3 = hist_ev[-1], hist_ev[-2], hist_ev[-3]
            roll_mean = np.mean([lag1, lag2, lag3])
            pct_change_1 = (lag1 - lag2) / lag2 if lag2 != 0 else 0
            pct_change_3 = (lag1 - lag3) / lag3 if lag3 != 0 else 0
            
            recent_cum = cum_ev[-6:]
            ev_slope = np.polyfit(range(len(recent_cum)), recent_cum, 1)[0] if len(recent_cum) == 6 else 0
            
            new_row = {
                'months_since_start': months_since,
                'county_encoded': cty_code,
                'ev_total_lag1': lag1,
                'ev_total_lag2': lag2,
                'ev_total_lag3': lag3,
                'ev_total_roll_mean_3': roll_mean,
                'ev_total_pct_change_1': pct_change_1,
                'ev_total_pct_change_3': pct_change_3,
                'ev_growth_slope': ev_slope
            }
            
            pred = model.predict(pd.DataFrame([new_row]))[0]
            future_rows_cty.append({"Date": forecast_date, "Predicted EV Total": round(pred)})
            
            hist_ev.append(pred)
            if len(hist_ev) > 6:
                hist_ev.pop(0)
            
            cum_ev.append(cum_ev[-1] + pred)
            if len(cum_ev) > 6:
                cum_ev.pop(0)
        
        hist_cum = cty_df[['Date', 'Electric Vehicle (EV) Total']].copy()
        hist_cum['Cumulative EV'] = hist_cum['Electric Vehicle (EV) Total'].cumsum()
        
        fc_df = pd.DataFrame(future_rows_cty)
        fc_df['Cumulative EV'] = fc_df['Predicted EV Total'].cumsum() + hist_cum['Cumulative EV'].iloc[-1]
        
        combined_cty = pd.concat([
            hist_cum[['Date', 'Cumulative EV']],
            fc_df[['Date', 'Cumulative EV']]
        ], ignore_index=True)
        combined_cty['County'] = cty
        comparison_data.append(combined_cty)
    
    # Combine all counties data for plotting
    comp_df = pd.concat(comparison_data, ignore_index=True)
    
    # Multi-dimensional comparison plot
    st.markdown("### 🌌 PARALLEL UNIVERSE COMPARISON")
    fig, ax = plt.subplots(figsize=(16, 9))
    fig.patch.set_facecolor('#0f0f23')
    ax.set_facecolor('#1a1a2e')
    
    neon_colors = ['#ff0080', '#00ff80', '#8000ff', '#ff8000', '#0080ff']
    
    for i, (cty, group) in enumerate(comp_df.groupby('County')):
        color = neon_colors[i % len(neon_colors)]
        ax.plot(group['Date'], group['Cumulative EV'], 
               marker='o', label=cty, linewidth=3, 
               markersize=6, color=color, alpha=0.9,
               markerfacecolor=color, markeredgecolor='white', markeredgewidth=1)
    
    ax.set_title("🌟 MULTI-DIMENSIONAL EV FORECAST MATRIX 🌟", 
                fontsize=20, color='#ff00ff', fontweight='bold', pad=30, fontfamily='monospace')
    ax.set_xlabel("TEMPORAL DIMENSION", color='#ff00ff', fontsize=16, fontfamily='monospace')
    ax.set_ylabel("EV QUANTUM UNITS", color='#ff00ff', fontsize=16, fontfamily='monospace')
    ax.grid(True, alpha=0.3, color='#ff00ff', linestyle='--')
    ax.tick_params(colors='#ffffff', labelsize=12)
    
    legend = ax.legend(title="PARALLEL COUNTIES", fontsize=12, title_fontsize=14, 
                      framealpha=0.8, facecolor='#1a1a2e', edgecolor='#ff00ff')
    legend.get_frame().set_facecolor('#1a1a2e')
    legend.get_title().set_color('#ff00ff')
    for text in legend.get_texts():
        text.set_color('#ffffff')
    
    plt.tight_layout()
    st.pyplot(fig)
    
    # Neural grid display of results
    st.markdown('<div class="neural-grid">', unsafe_allow_html=True)
    for cty in multi_counties:
        cty_df = comp_df[comp_df['County'] == cty].reset_index(drop=True)
        historical_total = cty_df['Cumulative EV'].iloc[len(cty_df) - forecast_horizon - 1]
        forecasted_total = cty_df['Cumulative EV'].iloc[-1]
        
        if historical_total > 0:
            growth_pct = ((forecasted_total - historical_total) / historical_total) * 100
            st.markdown(f"""
                <div class='neural-cell'>
                    <h4 style='color: #00ff00; margin: 0 0 10px 0;'>{cty}</h4>
                    <div style='font-size: 1.5rem; color: #ffff00; font-weight: bold;'>{growth_pct:.2f}%</div>
                    <p style='color: #e0e0e0; margin: 5px 0 0 0; font-size: 0.9rem;'>Growth Projection</p>
                </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# System Status
st.success("⚡ QUANTUM ANALYSIS COMPLETE - ALL SYSTEMS OPERATIONAL ⚡")

# Futuristic Footer
st.markdown("""
    <div class='footer-tech'>
        <h3 style='color: #00ffff; margin: 0 0 10px 0; font-family: Orbitron;'>🎓 NEURAL NETWORK POWERED</h3>
        <p style='color: #e0e0e0; margin: 0;'>Developed by **Madhusudan**  </p>
        <p style='color: #ff00ff; margin: 5px 0 0 0; font-size: 0.9rem;'>Advanced Machine Learning • Quantum Predictions • Future Analytics</p>
    </div>
""", unsafe_allow_html=True)
