# **Telco Customers Churn**

# Project Overview  
This project analyses customer data from a telecommunications company to identify key factors driving customer churn and to build a machine learning model capable of predicting churn.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
  
## Dataset Content
* Telco Customer Churn Dataset
Source: IBM Sample Dataset (Kaggle)

The dataset contains approximately 7,000 customer records with features including:

- Demographics
- Contract information
- Services subscribed
- Monthly charges
- Tenure
- Target variable: Churn

## Business Requirements
* The goal of this project is to analyse telecom customer data to understand the key factors that influence customer churn and develop a predictive model that identifies customers at risk of leaving the service.

- The specific business requirements are:
- Identify the main factors that contribute to customer churn.
- Analyse customer behaviour patterns related to contract type, tenure, and monthly charges.
- Develop a machine learning model capable of predicting customer churn.
- Present actionable insights through visualisations and dashboards to support business decision-making.
- Provide an interactive dashboard that allows stakeholders to explore churn patterns.

## Hypothesis and how to validate?
* Hypothesis 1

Customers with month-to-month contracts are more likely to churn than customers with long-term contracts.

Validation Method:
A Chi-Square test of independence will be performed to determine whether there is a statistically significant relationship between contract type and churn.

* Hypothesis 2

Customers with shorter tenure are more likely to churn than long-term customers.

Validation Method:
An Independent T-Test will compare the average tenure between churned and retained customers.

* Hypothesis 3

Customers with higher monthly charges are more likely to churn.

Validation Method:
A T-Test will compare the monthly charges between churned and non-churned customers.

## Project Plan
*The project followed a structured data analytics workflow consisting of:

+ Data Collection – The Telco Customer Churn dataset was sourced from a publicly available dataset.
+ Data Cleaning and Transformation – The data was cleaned, formatted, and prepared for analysis.
+ Exploratory Data Analysis – The dataset was analysed to identify patterns and relationships.
+ Data Visualisation – Graphical representations were created to communicate insights clearly.
+ Statistical Testing – Hypothesis testing was performed to validate findings.
+ Machine Learning – Predictive models were developed to forecast churn.
+ Dashboard Development – A visual dashboard was created for stakeholders.
  
*  Data Management 
Data was managed through the following stages:

+ Collection - The dataset was downloaded and stored in the project’s dataset/raw folder.
+ Processing - Data cleaning and transformations were performed in the ETL notebook. Missing values and incorrect data types were addressed.
+ Analysis -The cleaned dataset was analysed through exploratory data analysis and statistical testing.
+ Interpretation - Insights derived from analysis were visualised using charts and dashboards.
+ The cleaned dataset was stored in dataset/processed/cleaned_telco.csv to ensure reproducibility.
  
* Research methodologies used
  The following methodologies were used:

- Exploratory Data Analysis (EDA) to understand the dataset structure and patterns.
- Statistical hypothesis testing to validate observed relationships.
- Machine learning classification models to predict churn outcomes.

These methodologies were selected because they provide both descriptive and predictive insights, which are valuable for business decision-making.

## The rationale to map the business requirements to the Data Visualisations
* List your business requirements and a rationale to map them to the Data Visualisations

## Analysis techniques used

The following techniques were used:

+ Exploratory Data Analysis - Used to understand the structure and patterns in the dataset.
+ Data Visualisation - Used to identify relationships between features and churn behaviour.
+ Statistical Testing - Chi-Square tests and T-tests were used to validate whether observed relationships were statistically significant.
+ Machine Learning - Classification models were used to predict customer churn.
  
* The data analysis was structured in the following order:

- Data cleaning and transformation
- Exploratory analysis
- Visualisation of patterns
- Statistical validation
- Predictive modelling

This structure ensures that insights are validated before building predictive models.

* Data Limitations
  Some limitations of the dataset include:
- Limited behavioural variables
- Potential imbalance in churn classes

Alternative approaches could include:
- Random Forest or Gradient Boosting models
- Feature selection techniques
- Cross-validation for improved model robustness
  
* Generative AI Usage
  Generative AI tools were used to assist with:
- Project planning and ideation
- Code optimisation
- Debugging Python scripts
- Structuring documentation
  
## Ethical considerations
* Data Privacy - The dataset used is publicly available and contains no personally identifiable information.
* Bias and Fairness - Potential bias may exist in customer demographics or service usage patterns. Care was taken to avoid making discriminatory assumptions based on the data.
  
  ## Dashboard Design
  The dashboard was developed using Streamlit and structured into multiple pages to provide both data exploration and predictive functionality. The interface was designed to be simple, interactive, and accessible to both technical and non-technical users.

  ### Dashboard Pages
1. Home Page
Purpose: Provide an overview of the project.
Content includes:

* Project overview and description.
* Navigation sidebar.

2. Data Overview Page
Purpose: Allow users to explore the dataset and understand customer churn patterns.
Content includes:

Dataset preview (st.dataframe)
* Churn distribution chart
* KPI metrics (Total records, Churn rate, Number of features)

Feature distribution charts for:
* Monthly charges
* Total charges

Categorical churn analysis for:
* Contract
* Payment method
* Internet service
* Tenure group

3. Prediction Page
Purpose: Allow users to predict the churn risk of a customer using the trained machine learning model.
Content includes:

* Customer input form (tenure, monthly charges, total charges, contract type)
* Predict churn button
* Prediction result showing churn risk and probability.

During development, the tenure column was replaced with the tenure_group feature in visualisations because grouped tenure ranges provide clearer and more interpretable insights for users.

A minor limitation is that Streamlit’s built-in charts (st.bar_chart, st.line_chart) provide limited customisation compared to advanced libraries such as Plotly.

## Development Roadmap
### Challenges
* Aligning model input features with dashboard inputs.
* Creating clear visualisations from raw dataset features.

### Strategies
* Using feature encoding to match model inputs.
* Using tenure_group instead of raw tenure values.

## Deployment
The application is deployed using Heroku.

## Main Data Analysis Libraries
* Pandas – data loading and manipulation
Example:
df = pd.read_csv("Telco-Customer-Churn-Cleaned.csv")
* NumPy – numerical operations.
* Scikit-learn – machine learning model training and scaling.
* Joblib – loading the trained model and scaler.
* Streamlit – building the interactive dashboard.

## Learning Journey

This project has given me a hands-on experience in building a complete data science project from data analysis, to developing a machine learning model, and deploying a dashboard - the entire workflow basically. In this journey, i've consolidated my knowledge on cleaning data (the ETL process) and getting it ready for analysis, feature engineering, and model evaluation using Python libraries such as Pandas and Scikit-learn. I have also strenthened my skills in data and statistical analysis and visualisations, upon which i can obtain insights that that can be shared with diverse stakeholders.

One important part of the project was building an interactive dashboard using Streamlit and connecting the trained model to a simple interface where users can enter customer information and receive churn predictions. I also learned more about organising a project for deployment, including managing datasets, model files, and configuration files like requirements.txt, Procfile, and runtime.txt. The project has given me the confidence to build a professional project, while also highlighting the importance of presenting technical insights in a clear and accessible way for both technical and non-technical audiences.

## Credits
* Dataset from the IBM Telco Customer Churn dataset
* Documentation from Pandas, Scikit-learn, Streamlit
* LMS
* Generative AI (Github Copilot, ChatGPT)

## Acknowledgements 
Many thanks to Vasi, Mark and my colleagues who have been instrumental to the successful completion of this project