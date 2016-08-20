from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test_alive():
    return 'Server is UP'


@app.route('/fetchMarkets', methods=['GET'])
def fetch_markets():
    return None


@app.route('/fetchMarket', methods=['GET'])
def fetch_market():
    return None


@app.route('/fetchShares', methods=['GET'])
def fetch_shares():
    return None


@app.route('/fetchShare', methods=['GET'])
def fetch_share():
    return None


@app.route('/bidShare', methods=['POST'])
def bid_share():
    return None


@app.route('/retrieveShare', methods=['POST'])
def retrieve_share():
    return None


if __name__ == '__main__':
    app.run()
