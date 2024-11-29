from flask import Flask, render_template, jsonify, request
import pandas as pd
from prophet import Prophet
import os

app = Flask(__name__)

dataset_path = 'dataset.csv'
data = pd.read_csv(dataset_path)

# Data processing steps
filtered_data = data[data['JAHR'] <= 2020].copy()
filtered_data = filtered_data.dropna()
#shorten month to month value
filtered_data['MONAT'] = filtered_data['MONAT'].astype(str).str[-2:].astype(int)

@app.route('/')
def index():
    categories = ['Alkoholunfälle', 'Verkehrsunfälle', 'Fluchtunfälle']
    types = ['insgesamt', 'Verletzte und Getötete', 'mit Personenschäden']
    return render_template('index.html', categories=categories, types=types)

@app.route('/forecast', methods=['POST'])
def get_forecast():
    try:
        req_data = request.get_json()  # Ensure we are getting the JSON data
        category = req_data.get('category', 'Alkoholunfälle')
        _type = req_data.get('type', 'insgesamt')
        year = int(req_data.get('year', 2021))
        month = int(req_data.get('month', 1))

        category_data = filtered_data[
            (filtered_data['MONATSZAHL'] == category) &
            (filtered_data['AUSPRAEGUNG'] == _type)
        ]
        
        # Prepare data for Prophet model
        prophet_data = category_data[['JAHR', 'MONAT', 'WERT']]
        prophet_data.columns = ['ds', 'month', 'y']
        prophet_data['ds'] = pd.to_datetime(prophet_data['ds'].astype(str) + prophet_data['month'].astype(str).str.zfill(2), format='%Y%m')

        model = Prophet()
        model.fit(prophet_data)

        future = model.make_future_dataframe(periods=12, freq='M')
        forecast = model.predict(future)

        specific_prediction = forecast[(forecast['ds'].dt.year == year) & (forecast['ds'].dt.month == month)][['ds', 'yhat']]
        predicted_value = specific_prediction['yhat'].values[0]

        return jsonify({
       
            'predicted_value': predicted_value
        })

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': 'An error occurred during prediction.'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
