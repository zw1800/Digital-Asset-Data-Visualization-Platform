# Digital Asset Data Visualization Platform: Real Time Bitcoin-USDT Spot Price Tracker

This application fetches and displays real-time data of BTCUSDT spot price, 24-hour trading volume, 24-hour volatility, 24-hour price change percentage, and market cap. Since Binance is not available in the U.S and Binance U.S requires verification of SSN to get API key, I chose CoinMarketCap API to access the data. 

Getting price data at the granularity of seconds is not applicable from a free API key on CoinMarketCap, so I chose an interval of 5 seconds. The plots will be updated every 5 seconds.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Configuration

Set the API key for the CoinMarketCap API in the `main.py` file. (my api is provided as an example)

```python
api_key = 'YOUR_API_KEY'
```

Replace 'YOUR_API_KEY' with your actual API key.

## Running the Application

Run the application by executing the following command in the terminal (make sure the directory is correct).

```bash
python main.py
```

Navigate to the URL generated in your web browser

## Built With

* [Flask](https://flask.palletsprojects.com/) - The web framework used
* [CoinMarketCap API](https://coinmarketcap.com/api/) - The API used to fetch cryptocurrency data
* [Plotly.js](https://plotly.com/javascript/) - The JavaScript library used to plot the data
