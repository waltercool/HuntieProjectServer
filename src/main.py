from flask import Flask
from flask import request

app = Flask(__name__)


# No database test of backend.
@app.route('/test', methods=['GET'])
def test_alive():
    return 'Server is UP'


# Retrieve all Markets
@app.route('/fetchMarkets', methods=['GET'])
def fetch_markets():
    result = '';
    for key in request.args:
        result = result.join('['+key+','+request.args[key]+'],')
    return result


# Retrieve an specific market
@app.route('/fetchMarket', methods=['GET'])
def fetch_market():
    return 'Empty'


# Retrieve a specific stock info
@app.route('/fetchStock', methods=['GET'])
def fetch_share():
    return 'Empty'


# Buy a bid for a stock.
@app.route('/buyShare', methods=['POST'])
def buy_share():
    return 'Empty'


# Sell your bids for a specific stock.
@app.route('/sellStock', methods=['POST'])
def sell_share():
    return 'Empty'


# Retrieve all stocks bought
@app.route('/retrieveStocks', methods=['GET'])
def retrieve_stocks():
    return 'Empty'


# Handles login
@app.route('/login', methods=['POST'])
def login():
    # Needs Mongo communication, should be priority.
    return 'Empty'


if __name__ == '__main__':
    app.run()
