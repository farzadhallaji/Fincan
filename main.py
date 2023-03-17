#from flask import Flask, render_template, request, redirect, url_for


#import ccxt

#app = Flask(__name__)

#@app.route('/')
#@app.route('/home')
#@app.route('/index')
#def index():
    #return render_template('index.html')



#@app.route('/')
#def index():
    #Get a list of all available exchanges
    #exchanges = ccxt.exchanges

    #Render the exchanges list in a template
    #return render_template('index.html', exchanges=exchanges)


#@app.route('/config', methods=['GET', 'POST'])
#def config():
    #if request.method == 'POST':
        #api_key = request.form['api_key']
        #api_secret = request.form['api_secret']
        
        #Your code to use the API key and secret
        #...

        #return redirect(url_for('index'))
    #else:
        #return render_template('config.html')



#if __name__ == '__main__':
    #app.run()



from flask import Flask, render_template, request, redirect, url_for
from config_handler.config import ConfigHandler
import ccxt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# load the exchanges list
exchanges = ccxt.exchanges

# create instances of ConfigHandler
ch = ConfigHandler()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/config', methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        exchange = request.form['exchange']
        api_key = request.form['api_key']
        api_secret = request.form['api_secret']
        ch.set_config({'exchange': exchange, 'api_key':api_key, 'api_secret':api_secret})
        return redirect(url_for('stimulate'))

    return render_template('config.html', exchanges=exchanges)

@app.route('/update')
def update():
    #dh.update_data()
    return redirect(url_for('index'))

@app.route('/stimulate')
def stimulate():
    return "This is the stimulation page."

@app.route('/backtest')
def backtest():
    return "This is the backtesting page."

if __name__ == '__main__':
    app.run(debug=True)
