from flask import Flask, jsonify, render_template
import requests
import numpy as np

app = Flask(__name__)

# Set up API key and endpoint URL
api_key = 'a61856d9-8da1-43bd-8ce4-4cf648fc3c40' 
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# Set up headers for API request
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api_key,
}

# Set up parameters for API request
parameters = {
  'symbol':'BTC',
  'convert':'USDT'
}

# Initialize a list to store the last 24 hours of price data
historical_price = []

@app.route("/")
def index():
    """
    Renders the index.html template.

    Returns:
        A rendered HTML template.
    """
    return render_template('index.html')

@app.route("/btc_data")
def btc_data():
    """
    Retrieves data about Bitcoin (BTC) from the CoinMarketCap API.

    Returns:
        A JSON object containing the following information:
        - price: The current price of BTC in USDT.
        - volume_24h: The 24-hour trading volume of BTC in USDT.
        - percent_change_24h: The percentage change in price of BTC in the last 24 hours.
        - market_cap: The market capitalization of BTC in USDT.
    """
    # Send API request and retrieve response
    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    # Extract relevant data from the response
    price = data['data']['BTC']['quote']['USDT']['price']
    volume_24h = data['data']['BTC']['quote']['USDT']['volume_24h']
    percent_change_24h = data['data']['BTC']['quote']['USDT']['percent_change_24h']
    market_cap = data['data']['BTC']['quote']['USDT']['market_cap']

    # Add the new price to the list of price data
    historical_price.append(price)

    # If we have more than 24 hours (1440*12 5 seconds) of data, remove the oldest price
    if len(historical_price) > 1440*12:
        historical_price.pop(0)

    # Calculate 24 hour volatility 
    volatility = np.std(np.array(historical_price)) if len(historical_price) > 1 else 0

    # Return the extracted data as JSON
    return jsonify(price=price, volume_24h=volume_24h, percent_change_24h=percent_change_24h, market_cap=market_cap, volatility=volatility)

if __name__ == "__main__":
    app.run(debug=True)
