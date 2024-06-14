from flask import Flask, render_template, request
from calculation import value_calculation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_form():
    minprice = int(request.form['minprice'])
    maxprice = int(request.form['maxprice'])

    minmiles = int(request.form['minmiles'])
    maxmiles = int(request.form['maxmiles'])

    minyears = int(request.form['minyears'])
    maxyears = int(request.form['maxyears'])
    
    price_range = (minprice, maxprice)
    mileage_range = (minmiles, maxmiles)
    year_range = (minyears, maxyears)
    
    result = value_calculation(price_range=price_range, mileage_range=mileage_range, year_range=year_range)
    
    average = int(result['average_price'])
    median = int(result['median_price'])
    max = int(result['max_price'])
    min = int(result['min_price'])
    
    return render_template('index.html', var1 = minprice, var2 = maxprice, var3 = minmiles, var4 = maxmiles, var5 = minyears, var6 = maxyears, var7 = average, var8 = median, var9 = max, var10 = min)

if __name__ == '__main__':
    app.run()