from flask import Flask, render_template, request
from stats import average_price, median_price, max_price, min_price

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', var1 = int(average_price), var2 = int(median_price), var3 = int(max_price), var4 = int(min_price))

if __name__ == '__main__':
    app.run()