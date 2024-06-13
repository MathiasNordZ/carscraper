from flask import Flask, render_template, request
from calculation import calculator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_form():
    global minprice
    minprice = request.form['minprice']
    global maxprice
    maxprice = request.form['maxprice']

    global minmiles
    minmiles = request.form['minmiles']
    global maxmiles
    maxmiles = request.form['maxmiles']

    global minyears
    minyears = request.form['minyears']
    global maxyears
    maxyears = request.form['maxyears']

    return render_template('index.html', var1 = minprice, var2 = maxprice, var3 = minmiles, var4 = maxmiles, var5 = minyears, var6 = maxyears)

if __name__ == '__main__':
    app.run()