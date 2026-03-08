#!/bin/bash

# Telco Customer Churn Dashboard Runner
echo "🚀 Starting Telco Customer Churn Dashboard..."

# Check if virtual environment exists
if [ ! -d ".venv-1" ]; then
    echo "❌ Virtual environment .venv-1 not found!"
    echo "Please run: python -m venv .venv-1 && source .venv-1/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source .venv-1/bin/activate

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit not found in virtual environment!"
    echo "Please run: pip install streamlit"
    exit 1
fi

# Check if required files exist
if [ ! -f "model/churn_model.pkl" ]; then
    echo "❌ Model file not found: model/churn_model.pkl"
    exit 1
fi

if [ ! -f "model/scaler.pkl" ]; then
    echo "❌ Scaler file not found: model/scaler.pkl"
    exit 1
fi

if [ ! -f "dataset/Telco-Customer-Churn-Cleaned.csv" ]; then
    echo "❌ Dataset file not found: dataset/Telco-Customer-Churn-Cleaned.csv"
    exit 1
fi

# Run the Streamlit app
echo "🎯 Launching dashboard..."
echo "📱 Open your browser to: http://localhost:8501"
echo "🛑 Press Ctrl+C to stop the server"
echo ""

streamlit run app.py --server.headless true --server.port 8501