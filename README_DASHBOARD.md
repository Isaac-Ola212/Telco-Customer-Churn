# Telco Customer Churn Dashboard

A Streamlit-based dashboard for analyzing and predicting customer churn in a telecommunications company.

## Project Structure

```
├── app.py                 # Main Streamlit application
├── run_dashboard.sh       # Automated script to run the dashboard
├── model/                 # Directory containing trained models
│   ├── churn_model.pkl    # Trained Random Forest model
│   └── scaler.pkl         # Feature scaler
├── dataset/               # Directory containing datasets
│   └── Telco-Customer-Churn-Cleaned.csv  # Cleaned dataset
└── requirements.txt       # Python dependencies
```

## Quick Start

### Option 1: Use the automated script (Recommended)
```bash
./run_dashboard.sh
```

### Option 2: Manual setup
```bash
# Activate virtual environment
source .venv-1/bin/activate

# Run the Streamlit app
streamlit run app.py
```

## Prerequisites

- Python 3.8+
- Virtual environment with required packages installed
- Model files (`churn_model.pkl`, `scaler.pkl`) in `model/` directory
- Dataset (`Telco-Customer-Churn-Cleaned.csv`) in `dataset/` directory

## Features

- **Dashboard Overview**: Key metrics and statistics
- **Data Visualization**: Interactive charts and graphs
- **Model Predictions**: Churn prediction interface
- **Data Exploration**: Dataset preview and analysis

## Model Information

- **Algorithm**: Random Forest Classifier
- **Accuracy**: ~79%
- **Features**: Contract type, tenure, monthly charges, and other customer attributes

## Data

The dashboard uses the Telco Customer Churn dataset with the following key features:
- Customer demographics
- Service subscriptions
- Billing information
- Churn status

## Troubleshooting

### "Command not found: streamlit"
Make sure you're in the virtual environment:
```bash
source .venv-1/bin/activate
```

### "Model files not found"
Ensure the model files are in the correct location:
```bash
ls model/
# Should show: churn_model.pkl scaler.pkl
```

### "Dataset not found"
Ensure the dataset is in the correct location:
```bash
ls dataset/
# Should show: Telco-Customer-Churn-Cleaned.csv
```

### Port already in use
If port 8501 is busy, specify a different port:
```bash
streamlit run app.py --server.port 8502
```

## Development

To extend the dashboard:

1. Edit `app.py` to add new features
2. Add new pages using `st.sidebar` navigation
3. Include additional visualizations and metrics
4. Add prediction interfaces for individual customers

## Deployment

For production deployment, consider:
- Using Docker containers
- Setting up proper authentication
- Optimizing model loading and caching
- Adding monitoring and logging