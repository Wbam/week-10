from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load the datasets
prices_df = pd.read_csv(r'/home/bamw/Downloads/Compressed/data-20241101T120533Z-001/data/Copy of BrentOilPrices.csv')
events_df = pd.read_csv(r'/home/bamw/Downloads/events.csv')

@app.route('/')
def home():
    return "Welcome to the Brent Oil Prices Dashboard!"

@app.route('/api/prices', methods=['GET'])
def get_prices():
    return jsonify(prices_df.to_dict(orient='records'))

@app.route('/api/events', methods=['GET'])
def get_events():
    return jsonify(events_df.to_dict(orient='records'))

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    
    metrics = {
        "ADF_Brent_Price": {"Statistic": -2.4903, "p_value": 0.1178}, 
        "ADF_GDP": {"Statistic": 1.2326, "p_value": 0.9962},         
        "RMSE": 0.5,  
        "MAE": 0.3    
    }
    return jsonify(metrics)

@app.route('/api/forecast', methods=['GET'])
def get_forecast():
    forecast_data = {
        "date": ["2024-01-01", "2024-01-02", "2024-01-03"],
        "predicted_price": [67.77, 68.50, 69.25]  
    }
    return jsonify(forecast_data)

if __name__ == '__main__':
    app.run(debug=True)
