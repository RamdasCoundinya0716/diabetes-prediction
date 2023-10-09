# Diabetes Prediction ML App

## Project Overview

Diabetes Prediction ML App is a machine learning application that predicts the likelihood of a person having diabetes based on various health-related features. The application uses logistic regression, decision tree, random forest classifier, and naive Bayes algorithms for prediction.

## Installation Instructions

To run this application locally or in a container, follow these steps:

### Prerequisites

- Python 3.10.11
- Ensure you have the required dependencies installed:
- Requirements are present in requirements.txt file.

### Running in a Docker Container
1) Pull the Docker image: docker pull ram0716/diabetes-ml-image:v1
2) Run the Docker container: docker run -p 8888:8888 ram0716/diabetes-ml-image:v1
3) Visit http://localhost:8888 in your web browser to access the application.

### Dependencies
Python 3.10.11
NumPy 1.19.5
Pandas 1.1.5
Matplotlib 3.3.4
Scikit-Learn 0.24.1

### Link to Docker Image on Docker Hub
https://hub.docker.com/r/ram0716/diabetes-ml-image
