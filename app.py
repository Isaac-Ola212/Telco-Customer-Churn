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

        # Display summary statistics 
        st.subheader("📊 Statistical Summary")

        col4, col5, col6 = st.columns(3)

        with col4:
            st.metric("Mean Monthly Charges", round(df["MonthlyCharges"].mean(), 2))

        with col5:
            st.metric("Median Monthly Charges", round(df["MonthlyCharges"].median(), 2))

        with col6:
            st.metric("Std Dev Monthly Charges", round(df["MonthlyCharges"].std(), 2))


        col7, col8 = st.columns(2)

        with col7:
            st.metric("Variance Monthly Charges", round(df["MonthlyCharges"].var(), 2))

        with col8:
            st.metric("Average Tenure", round(df["tenure"].mean(), 1))


        st.subheader("Detailed Statistical Table")

        st.dataframe(
            df[['tenure','MonthlyCharges','TotalCharges']].describe()
        )

        # Additional distribution charts
        st.subheader("Feature Distributions")

        # Numerical features
        numerical_cols = ['MonthlyCharges', 'TotalCharges']
        for col in numerical_cols:
            if col in df.columns:
                st.subheader(f"Distribution of {col}")
                st.bar_chart(df[col].value_counts(bins=20))

        # Categorical features relevant to churn
        categorical_cols = ['Contract', 'PaymentMethod', 'InternetService', 'tenure_group']
        for col in categorical_cols:
            if col in df.columns:
                st.subheader(f"Churn by {col}")
                churn_by_cat = df.groupby([col, 'Churn']).size().unstack().fillna(0)
                st.bar_chart(churn_by_cat)

        # Tenure vs Churn
        st.subheader("Churn by Tenure Group")
        tenure_churn = df.groupby(['tenure_group', 'Churn']).size().unstack().fillna(0)
        st.bar_chart(tenure_churn)

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
            # Get the feature columns from the dataset (excluding target if present)
            feature_cols = [col for col in df.columns if col != 'Churn']

            # Create a full input DataFrame with default values
            input_data = pd.DataFrame(index=[0], columns=feature_cols)
            input_data = input_data.fillna(0)  # Fill numerical with 0, categorical with appropriate defaults

            # Set default values for categorical features (assuming 'No' or most common)
            categorical_defaults = {
                'gender': 'Female',
                'Partner': 'No',
                'Dependents': 'No',
                'PhoneService': 'Yes',
                'MultipleLines': 'No',
                'InternetService': 'DSL',
                'OnlineSecurity': 'No',
                'OnlineBackup': 'No',
                'DeviceProtection': 'No',
                'TechSupport': 'No',
                'StreamingTV': 'No',
                'StreamingMovies': 'No',
                'Contract': 'Month-to-month',
                'PaperlessBilling': 'Yes',
                'PaymentMethod': 'Electronic check',
                'SeniorCitizen': 0
            }
            for col, default in categorical_defaults.items():
                if col in input_data.columns:
                    input_data[col] = default

            # Update with user inputs
            input_data['tenure'] = tenure
            input_data['MonthlyCharges'] = monthly_charges
            input_data['TotalCharges'] = total_charges
            input_data['Contract'] = contract

            # One-hot encode the input data to match training
            input_encoded = pd.get_dummies(input_data, drop_first=True)

            # Get the expected features from the scaler (assuming scaler was fitted on encoded data)
            # If not, this might need adjustment; for now, assume scaler's feature_names_in_ if available
            if hasattr(scaler, 'feature_names_in_'):
                expected_features = list(scaler.feature_names_in_)
            else:
                # Fallback: assume based on common encoding; adjust as needed
                expected_features = input_encoded.columns.tolist()

            # Ensure all expected columns are present
            for col in expected_features:
                if col not in input_encoded.columns:
                    input_encoded[col] = 0

            # Reorder to match expected
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