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

That's it! You can now use the Diabetes Prediction ML App to make predictions based on health-related features.
