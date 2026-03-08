import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Set page configuration
st.set_page_config(
    page_title="Telco Customer Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load models and data
@st.cache_resource
def load_models():
    """Load the trained model and scaler"""
    try:
        ml_model = joblib.load('model/churn_model.pkl')
        scaler = joblib.load('model/scaler.pkl')
        return ml_model, scaler
    except FileNotFoundError:
        st.error("Model files not found. Please ensure churn_model.pkl and scaler.pkl are in the model/ directory.")
        return None, None

@st.cache_data
def load_data():
    """Load the dataset"""
    try:
        df = pd.read_csv('dataset/Telco-Customer-Churn-Cleaned.csv')
        return df
    except FileNotFoundError:
        st.error("Dataset not found. Please ensure Telco-Customer-Churn-Cleaned.csv is in the dataset/ directory.")
        return None

def show_home_page():
    """Display the home page"""
    st.header("🏠 Project Overview")
    st.write("""
    This project analyses telecom customer behaviour and predicts churn risk
    using machine learning.

    ### Key Features:
    - 📊 Interactive data visualizations
    - 🤖 Machine learning predictions
    - 📈 Customer churn analysis
    - 🎯 Risk assessment tools
    """)

def show_data_overview(df):
    """Display data overview page"""
    st.header("📊 Data Overview")

    if df is not None:
        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        st.subheader("Churn Distribution")
        churn_counts = df["Churn"].value_counts()
        st.bar_chart(churn_counts)

        # Additional statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Records", len(df))
        with col2:
            churn_rate = (df['Churn'].sum() / len(df)) * 100
            st.metric("Churn Rate", f"{churn_rate:.1f}%")
        with col3:
            st.metric("Features", len(df.columns))

def show_prediction_page(ml_model, scaler, df):
    """Display prediction page"""
    st.header("🔮 Make Prediction")

    if ml_model is None or scaler is None or df is None:
        st.error("Models or data not loaded properly.")
        return

    st.subheader("Enter Customer Details")

    # Create input form
    col1, col2 = st.columns(2)

    with col1:
        tenure = st.slider("Tenure (Months)", 0, 72, 12)
        monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 70.0)

    with col2:
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        total_charges = st.number_input("Total Charges ($)", 0.0, 10000.0, 1000.0)

    # Make prediction button
    if st.button("🔍 Predict Churn Risk", type="primary"):
        try:
            # Prepare input data - this needs to match the training data structure
            # For now, we'll use a simplified approach
            input_data = pd.DataFrame({
                'tenure': [tenure],
                'MonthlyCharges': [monthly_charges],
                'TotalCharges': [total_charges],
                'Contract': [contract]
            })

            # One-hot encode categorical variables to match training data
            input_encoded = pd.get_dummies(input_data, drop_first=True)

            # Ensure all expected columns are present (add missing ones with 0)
            expected_features = ['tenure', 'MonthlyCharges', 'TotalCharges',
                               'Contract_One year', 'Contract_Two year']

            for col in expected_features:
                if col not in input_encoded.columns:
                    input_encoded[col] = 0

            # Reorder columns to match training data
            input_encoded = input_encoded[expected_features]

            # Scale the input
            input_scaled = scaler.transform(input_encoded)

            # Make prediction
            prediction = ml_model.predict(input_scaled)
            probability = ml_model.predict_proba(input_scaled)[0][1]

            # Display results
            st.subheader("🎯 Prediction Results")

            if prediction[0] == 1:
                st.error(f"⚠️ **High Churn Risk Detected!**")
                st.write(f"Churn Probability: **{probability:.1%}**")
                st.write("💡 **Recommendation:** Consider offering retention incentives.")
            else:
                st.success(f"✅ **Low Churn Risk**")
                st.write(f"Churn Probability: **{probability:.1%}**")
                st.write("👍 Customer appears satisfied with the service.")

        except Exception as e:
            st.error(f"❌ Error making prediction: {str(e)}")
            st.info("Please ensure all input fields are filled correctly.")

def main():
    st.title("📊 Telco Customer Churn Dashboard")
    st.markdown("---")

    # Load data and models
    df = load_data()
    ml_model, scaler = load_models()

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Select Page",
        ["Home", "Data Overview", "Make Prediction"]
    )

    # Display loading status
    if df is not None and ml_model is not None and scaler is not None:
        st.sidebar.success("✅ All systems operational")

        # Route to different pages
        if page == "Home":
            show_home_page()
        elif page == "Data Overview":
            show_data_overview(df)
        elif page == "Make Prediction":
            show_prediction_page(ml_model, scaler, df)
    else:
        st.sidebar.error("❌ System initialization failed")
        st.error("❌ Failed to load required files. Please check the model/ and dataset/ directories.")

if __name__ == "__main__":
    main()