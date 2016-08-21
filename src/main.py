from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test_alive():
    return 'Server is UP'


@app.route('/fetchMarkets', methods=['GET'])
def fetch_markets():
    return 'Empty'


@app.route('/fetchMarket', methods=['GET'])
def fetch_market():
    return 'Empty'


@app.route('/fetchShares', methods=['GET'])
def fetch_shares():
    return 'Empty'


@app.route('/fetchShare', methods=['GET'])
def fetch_share():
    return 'Empty'


@app.route('/bidShare', methods=['POST'])
def bid_share():
    return 'Empty'


@app.route('/retrieveShare', methods=['POST'])
def retrieve_share():
    return 'Empty'


if __name__ == '__main__':
    app.run()
