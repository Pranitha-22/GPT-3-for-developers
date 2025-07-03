from gpt_utils import ask_gpt

def generate_resume(text=None):
    experience_details = """
I am currently taking an AI and Data Science course. I have hands-on experience with Python, SQL, Power BI, Excel, and Machine Learning. 
I worked on multiple real-time datasets such as Titanic, home prices, cancer, iris, heart disease, diabetes.
I also developed:
- Loan Prediction using Streamlit app
- House Price Prediction using regression models
- Customer Churn Prediction using classification
- Streamlit-based Library Management System
- GPT-3 powered application that generates Python code for EDA, visualizations, resumes, and meeting summaries

I have a strong foundation in statistics, probability, linear algebra, and calculus. I am actively learning by building projects and solving real-world problems.
    """

    prompt = f"""
You are a professional resume writer.

Write a clean, internship-style resume for someone based on the following details:

{experience_details}

The resume should include the following sections with bullet points and proper formatting:

- **Name**: Pranitha Theegela
- **Location**: Koratla, Telangana, India
- **Contact Info**: https://github.com/PranithaTheegela

- **Objective**:
Motivated and detail-oriented aspiring Data Scientist with a strong foundation in statistics, probability, linear algebra, and calculus. Passionate about leveraging data-driven insights to solve real-world problems. Seeking an internship opportunity to apply and further develop my analytical and machine learning skills.

- **Education**:
Bachelor of Technology (B.Tech) in Computer Science  
JNTU Hyderabad, 2022

- **Skills**:

  • Languages & Tools:  
  Python, SQL, Excel, Power BI, Streamlit, Git, Google Colab

  • Libraries & Frameworks:  
  Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost

  • Concepts:  
  Machine Learning, Exploratory Data Analysis (EDA), Data Visualization, Supervised & Unsupervised Learning, Regression, Classification, Statistics, Probability, Linear Algebra, Calculus

- **Projects**:

  1. **Customer Churn Prediction**
     - Analyzed customer behavior to predict churn using classification models
     - Conducted EDA and feature engineering for better insights
     - Achieved high accuracy using Random Forest and XGBoost classifiers

  2. **House Price Prediction Web App**
     - Built an interactive Streamlit web app for predicting house prices
     - Used regression models to estimate prices based on location, size, and age
     - Integrated data visualization for better user experience

  3. **Adult Census Income Classification**
     - Cleaned and processed census data to classify income levels
     - Applied logistic regression and decision tree models
     - Evaluated model performance using precision, recall, and F1-score

  4. **Library Management System (Ongoing)**
     - Developing a Streamlit-based app to manage books, members, and borrowing records
     - Implementing features like search, add, update, and delete operations using Python

  5. **GPT-powered Code Generator (VS Code Project)**
     - Created a tool that uses GPT-3 to generate EDA and visualization code from user prompts
     - Includes features for resume generation, interview question creation, and meeting summarization

6.Conditional Generative Adversarial Network (CGAN):
       - Developed a CGAN to generate fake images from synthetic data

7.Object Classification for automated CCTV

- **Certifications**:
Principles of Generative AI Certification

Artificial Intelligence Primer Certification

OpenAI Generative Pre-trained Transformer 3 (GPT-3) for developers

Introduction to Artificial Intelligence

Deep Learning for Developer

Prompt Engineering

Artificial Intelligence

AWS AI Practitioner: Basic AI Concepts and Terminologies

AWS-DGL-SS-Building a Generative AI-Ready Organization

AI & Data Science Certification Course (Ongoing – 70% completed)
    """

    return ask_gpt(prompt)
