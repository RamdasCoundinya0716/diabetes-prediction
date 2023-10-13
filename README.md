# Diabetes Prediction ML App

## Project Overview

Diabetes Prediction ML App is a machine learning application that predicts the likelihood of a person having diabetes based on various health-related features. The application uses logistic regression, decision tree, random forest classifier, and naive Bayes algorithms for prediction.

## Usage Guide

The Diabetes Prediction ML App is designed to predict the likelihood of a person having diabetes based on health-related features. Follow these steps to run the application either locally or in a Docker container.

### Local Installation:

1. **Prerequisites:**
    - Ensure you have Python 3.10.11 installed on your machine.
    - Also, clone this repo to understand code.

2. **Install Dependencies:**
    - Open your terminal.
    - Navigate to the project directory.
    - Run the following command to install the required dependencies:
        **pip install -r requirements.txt**

3. **Run the App:**
    - Execute the following command to run the application locally:
    - **python flask_app.py**
    - Visit http://127.0.0.1:5000 in your web browser to access the application.

### Docker Installation:

1. **Prerequisites:**
    - Ensure you have Docker installed on your machine.

2. **Pull Docker Image:**
    - Run the following command to pull the Docker image from Docker Hub:
    - **docker pull ram0716/diabetes-prediction:v1**


3. **Run Docker Container:**
    - Execute the following command to run the Docker container:
    - **docker run -p 5000:5000 ram0716/diabetes-prediction:v1**
    - Visit http://127.0.0.1:5000 in your web browser to access the application.

### Application Usage:

- Once the application is running, you will be presented with a web interface.
- Fill in the health-related features in the provided form.
- Click on the "Predict" button to get predictions from the logistic regression, decision tree, random forest classifier, and naive Bayes algorithms.
- View the predictions and explore the results on the web interface.

### Example Outputs:

After entering the health-related features and clicking on "Predict," you'll receive the final predictions. Let's look at some examples:

1. **Output 0 (Normal Male Patient):**
   - Example Input (Normal Male):
     - Pregnancies: 0  # Not applicable for males
     - Glucose: 100
     - Blood Pressure: 70
     - Skin Thickness: 22
     - Insulin: 80
     - BMI: 24
     - Diabetes Pedigree Function: 0.25
     - Age: 30
   - All Algorithms: Predicts 0

   Interpretation: A prediction of 0 suggests a lower likelihood of diabetes for a normal male individual.

2. **Output 0 (Normal Female with 1 Pregnancy):**
   - Example Input (Normal Female - 1 Pregnancy):
     - Pregnancies: 1
     - Glucose: 110
     - Blood Pressure: 68
     - Skin Thickness: 26
     - Insulin: 75
     - BMI: 22
     - Diabetes Pedigree Function: 0.28
     - Age: 28
   - All Algorithms: Predicts 0

   Interpretation: A prediction of 0 suggests a lower likelihood of diabetes for a normal female with one pregnancy.

3. **Output 1 (Higher Glucose Level):**
   - Example Input (Higher Glucose Level):
     - Pregnancies: 3
     - Glucose: 170
     - Blood Pressure: 75
     - Skin Thickness: 28
     - Insulin: 120
     - BMI: 26
     - Diabetes Pedigree Function: 0.38
     - Age: 35
   - All Algorithms: Predicts 1

   Interpretation: A prediction of 1 indicates a higher likelihood of diabetes due to the higher glucose levels.

4. **Output 1 (Higher BMI):**
   - Example Input (Higher BMI):
     - Pregnancies: 2
     - Glucose: 130
     - Blood Pressure: 80
     - Skin Thickness: 30
     - Insulin: 90
     - BMI: 32
     - Diabetes Pedigree Function: 0.42
     - Age: 40
   - All Algorithms: Predicts 1

   Interpretation: A prediction of 1 suggests a higher likelihood of diabetes due to the elevated BMI.

Feel free to use these examples to illustrate how the model responds to different health-related features and scenarios.

**That's it! You can now use the Diabetes Prediction ML App to make predictions based on health-related features.**
