# House Price Predictor

A Streamlit-based machine learning app for predicting house prices from property details such as bedrooms, bathrooms, living area, condition, and nearby schools.

## Live App

Open the deployed app here:

`https://houseprice-6xvyxsm5ayvfvsgzou695g.streamlit.app/`

## Features

- Predicts house prices using a trained machine learning model
- Clean Streamlit dashboard layout
- Interactive 3D house view using Three.js
- 3D price surface visualization using Plotly
- Simple input form for property details

## Tech Stack

- Python
- Streamlit
- NumPy
- scikit-learn
- Joblib
- Plotly
- Three.js

## Project Files

- `app.py` - main Streamlit application
- `Random_search.pkl` - trained machine learning model
- `House Price India (1).csv` - dataset used in the project
- `requirements.txt` - Python dependencies

## Run Locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the Streamlit app:

```bash
streamlit run app.py
```

## Input Fields

- Bedrooms
- Bathrooms
- Living Area (sq ft)
- Condition
- Nearby Schools

## Output

The app predicts the estimated house price and also shows a 3D surface chart based on living area and house condition.
