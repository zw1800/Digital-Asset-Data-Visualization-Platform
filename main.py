from flask import Flask, jsonify, render_template
import requests

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

    # Return the extracted data as JSON
    return jsonify(price=price, volume_24h=volume_24h, percent_change_24h=percent_change_24h, market_cap=market_cap)

if __name__ == "__main__":
    app.run(debug=True)
