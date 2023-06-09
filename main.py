from flask import Flask, render_template, request, redirect, url_for
import ccxt


from views.api_handler import api_handler
from constans.candle import TimeFrames
from constans.index import IndexItems


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# load the exchanges list
exchanges = ccxt.exchanges


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', items=IndexItems)


@app.route('/config', methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        exchange = request.form['exchange']
        api_key = request.form['api_key']
        api_secret = request.form['api_secret']
        api_handler.insert_config(exchange, api_key, api_secret)
        return redirect(url_for('update_data'))

    return render_template('config.html', exchanges=exchanges)

@app.route('/update_data', methods=['GET', 'POST'])
def update_data():
    if request.method == 'GET':
        apis = api_handler.read_configs()
        # exchange = ccxt.binance()  # replace with your desired exchange
        # exchange.load_markets()
        # symbols = list(exchange.markets.keys())
        symbols = ['BTCUSDT']
        return render_template('update_data.html', 
                               exchanges=[api.exchange for api in apis], 
                               currencies= symbols, TFs=TimeFrames)
    return render_template('index.html')

@app.route('/preprocess_data')
def preprocess_data():
    return "This is the preprocess_data page."

@app.route('/stimulate')
def stimulate():
    return "This is the stimulation page."

@app.route('/backtest')
def backtest():
    return "This is the backtesting page."

if __name__ == '__main__':
    app.run(debug=True)
