from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    close = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(10), nullable=False)

@app.route('/')
def index():
    lang = request.args.get('lang', 'zh')
    return render_template('index.html', lang=lang)

@app.route('/stocks')
def stocks():
    records = Stock.query.all()
    return render_template('stocks.html', records=records)

@app.route('/stock/<symbol>')
def stock(symbol):
    data = Stock.query.filter_by(symbol=symbol).all()
    if not data:
        return render_template('error.html', error="找不到股票資料！")
    return render_template('stock.html', symbol=symbol, data=data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error="頁面未找到！"), 404

if __name__ == '__main__':
    db.create_all()  # 确保数据库创建
    app.run(port=10000, host='0.0.0.0',debug=True)
