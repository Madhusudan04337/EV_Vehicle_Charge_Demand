# ⚡ EV NEXUS FORECASTER

> **Advanced Neural Prediction System for Electric Vehicle Adoption Analysis**

A futuristic Streamlit web application that leverages machine learning to predict electric vehicle (EV) adoption trends across Washington State counties. Built with cutting-edge data science techniques and an immersive user interface.

![EV Forecaster Demo](https://img.shields.io/badge/Status-Active-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red) ![ML](https://img.shields.io/badge/ML-Scikit--Learn-orange)

## 🌟 Features

### 🎯 Core Functionality
- **Single County Analysis**: Deep dive into individual county EV adoption patterns
- **Multi-County Comparison**: Parallel analysis of up to 3 counties simultaneously
- **36-Month Forecasting**: Advanced machine learning predictions for 3-year outlook
- **Interactive Visualizations**: Dynamic charts with historical and predicted data
- **Real-time Processing**: Instant analysis with cached data loading

### 🎨 User Experience
- **Futuristic UI Design**: Electric-themed interface with neon colors and animations
- **Responsive Layout**: Optimized for desktop and mobile viewing
- **Interactive Elements**: Hover effects, glowing borders, and smooth transitions
- **Professional Charts**: Dark-themed visualizations with electric color schemes

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
pip package manager
```

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd ev-forecasting-project
```

2. **Install dependencies**
```bash
pip install streamlit pandas numpy joblib matplotlib
```

3. **Prepare your data files**
   - Place `forecasting_ev_model.pkl` in the project root
   - Place `preprocessed_ev_data.csv` in the project root
   - Place `ev-car-factory.jpg` in the project root

4. **Run the application**
```bash
streamlit run app.py
```

5. **Access the app**
   - Open your browser to `http://localhost:8501`
   - Start analyzing EV adoption trends!

## 📁 Project Structure

```
ev-forecasting-project/
│
├── app.py                          # Main Streamlit application
├── forecasting_ev_model.pkl        # Pre-trained ML model
├── preprocessed_ev_data.csv         # Historical EV data
├── ev-car-factory.jpg              # Hero image
├── README.md                       # Project documentation
└── requirements.txt                # Python dependencies
```

## 🔧 Technical Architecture

### Data Pipeline
1. **Data Loading**: Cached CSV data loading with Pandas
2. **Feature Engineering**: Lag features, rolling means, percentage changes
3. **Model Prediction**: Scikit-learn based forecasting model
4. **Visualization**: Matplotlib with custom styling

### Machine Learning Model
- **Algorithm**: Pre-trained regression model (stored in PKL format)
- **Features**: 
  - Temporal features (months since start)
  - Lag features (1, 2, 3 months)
  - Rolling statistics (3-month moving average)
  - Growth metrics (percentage changes, slopes)
- **Output**: Monthly EV adoption predictions

### Key Technologies
- **Frontend**: Streamlit with custom CSS/HTML
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn (joblib)
- **Visualization**: Matplotlib
- **Styling**: Custom CSS with animations and gradients

## 📊 Data Requirements

### Input Data Format (`preprocessed_ev_data.csv`)
```csv
Date,County,Electric Vehicle (EV) Total,county_encoded,months_since_start
2020-01-01,King,1500,1,1
2020-02-01,King,1650,1,2
...
```

### Required Columns
- `Date`: Timestamp in YYYY-MM-DD format
- `County`: County name (string)
- `Electric Vehicle (EV) Total`: Monthly EV count (integer)
- `county_encoded`: Numerical county identifier (integer)
- `months_since_start`: Sequential month counter (integer)

## 🎨 Customization Guide

### Branding & Text
```python
# Update app title
<h1 class='electric-title'>⚡ YOUR APP NAME</h1>

# Update footer
<p style='color: #e0e0e0;'>Created by YOUR NAME</p>
```

### Color Scheme
```css
/* Primary colors */
--electric-blue: #00ffff
--electric-magenta: #ff00ff
--electric-yellow: #ffff00
--electric-green: #00ff00
```

### Page Configuration
```python
st.set_page_config(
    page_title="Your App Title",
    layout="wide"
)
```

## 📈 Usage Examples

### Single County Analysis
1. Select a county from the dropdown
2. View the interactive forecast chart
3. Analyze the growth percentage prediction

### Multi-County Comparison
1. Use the multi-select widget
2. Choose up to 3 counties
3. Compare trends in the parallel analysis chart
4. Review growth projections in the neural grid

## 🔍 Model Performance

The forecasting model uses advanced feature engineering including:
- **Temporal Features**: Seasonal and trend components
- **Lag Variables**: Historical dependency modeling
- **Statistical Features**: Rolling averages and growth rates
- **Encoded Categories**: County-specific patterns

## 🛠️ Development

### Adding New Features
1. **New Visualizations**: Add charts in the plotting sections
2. **Enhanced Styling**: Modify CSS in the `st.markdown` sections
3. **Additional Metrics**: Extend the feature engineering pipeline
4. **Export Functionality**: Add data download capabilities

### Code Structure
- **Styling**: Lines 15-200 (CSS and animations)
- **Data Loading**: Lines 95-105 (Cached data functions)
- **Forecasting Logic**: Lines 130-180 (ML predictions)
- **Visualizations**: Lines 200-350 (Chart generation)
- **UI Components**: Throughout (Streamlit widgets)

## 🚨 Troubleshooting

### Common Issues

**Model file not found**
```bash
FileNotFoundError: forecasting_ev_model.pkl
```
*Solution*: Ensure the PKL file is in the project root directory

**Data loading errors**
```bash
FileNotFoundError: preprocessed_ev_data.csv
```
*Solution*: Verify CSV file exists and has required columns

**Import errors**
```bash
ModuleNotFoundError: No module named 'streamlit'
```
*Solution*: Install dependencies with `pip install -r requirements.txt`

### Performance Optimization
- Data is cached using `@st.cache_data` decorator
- Large datasets are processed efficiently with Pandas
- Charts are generated on-demand to reduce memory usage

## 📝 Requirements

### Python Dependencies
```txt
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.24.0
joblib>=1.3.0
matplotlib>=3.6.0
scikit-learn>=1.3.0
```

### System Requirements
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 100MB for application and data
- **Browser**: Modern web browser with JavaScript enabled

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🎓 Academic Context

**Project Type**: Machine Learning & Data Science Application  
**Domain**: Transportation Analytics & Sustainability  
**Techniques**: Time Series Forecasting, Feature Engineering, Web Development  
**Tools**: Python, Streamlit, Scikit-learn, Pandas, Matplotlib  

---

**EV Forecasting System | Machine Learning Powered**
