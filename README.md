# DPS_AI_deploy

description: |
  This project is done as part of AI-Challenge by DPS Munich.
  It analyzes traffic accident data from Munich and implements a prediction model using the Prophet library. 
  It includes data preprocessing, historical analysis, and a web application built with Flask to forecast traffic accidents.

# Data Source
data_source: 
  - url: https://opendata.muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7
  - description: |
      The dataset contains monthly traffic accident statistics for Munich.

# Workflow
steps:
  - step: Data Analysis in Google Colab
    details:
      - Downloaded dataset from the provided URL.
      - Performed data cleaning and removed null values.
      - Limited data to years up to 2020.
      - Created a new column 'date' combining year (JAHR) and month (MONAT).

  - step: Historical Analysis
    details:
      - Plotted line charts and bar charts for yearly accidents by category.

  - step: Data Subsetting and Model Selection
    details:
      - Created subsets for target categories and accident types.
      - Tested the dataset with SARIMA, Prophet, and LSTM models.
      - Observed that:
          - LSTM performed poorly.
          - Prophet and SARIMA yielded predictions close to actual values.
      - Chose the Prophet model for its better performance.

  - step: Web Application Development
    details:
      - Set up a Flask environment to deploy the prediction model.
      - Defined routes to render an HTML template.
      - Used POST requests and JSON input for prediction:
        input_format: |
          {
            "year": 2020,
            "month": 10
          }
      - Returned output in the following format:
        output_format: |
          {
            "prediction": <value>
          }
  - step: Deployment
    details:
      - Set Up Google Cloud Environment on GCP and authenticate Google Cloud SDK.
      - Containerize the Application with DOCKER.
      - Initialize project, set up permissions and apis, deploy the app.

# Tech Stack
tech_stack:
  - Python
  - Flask
  - Prophet
  - Google Colab
  - Matplotlib (for visualizations)
  - Google Cloud Platform (for deployment)

# Usage
usage:
  - Clone the repository.
  - Install dependencies listed in `requirements.txt`.
  - Run the Flask app using `python app.py`. on localhost
  - Send a POST request to the app's endpoint with the desired input format to get predictions.
  - Alternatively visit `https://dps-310184006355.asia-south1.run.app` to check out the webapp

# Future Enhancements
future_plans:
  - Explore additional models for better accuracy.
  - Extend the dataset to include newer data.
  - Develop a more robust front-end interface for better usability.
