from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

# 加载环境变量
load_dotenv()

app = Flask(__name__)

# 从环境变量获取 API 密钥
API_KEY_1 = os.getenv('MARKETSTACK_API_KEY')
API_KEY_2 = os.getenv('MARKETSTACK_API_KEY_2')
BASE_URL = 'http://api.marketstack.com/v1'

# 路由：主页
@app.route('/')
def index():
    lang = request.args.get('lang', 'zh')  # 选择语言
    return render_template('index.html', lang=lang)

# 路由：股票查询
@app.route('/search', methods=['POST'])
def search_stock():
    stock_symbol = request.form['symbol'].upper()
    endpoint = f'{BASE_URL}/eod'
    params = {
        'access_key': API_KEY_1,
        'symbols': stock_symbol,
        'limit': 100
    }

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and data['data']:
            return render_template('result.html', data=data['data'], symbol=stock_symbol)
        else:
            return render_template('error.html', error='未找到该股票的记录。')
    else:
        return render_template('error.html', error=response.text)

# 路由：API股票数据
@app.route('/api/stock', methods=['GET'])
def api_stock():
    stock_symbol = request.args.get('symbol').upper()
    endpoint = f'{BASE_URL}/eod'
    params = {
        'access_key': API_KEY_1,
        'symbols': stock_symbol,
        'limit': 100
    }

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': response.text}), response.status_code

# 路由：列出所有股票记录
@app.route('/stocks', methods=['GET'])
def list_stocks():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    endpoint = f'{BASE_URL}/eod'
    params = {
        'access_key': API_KEY_2,
        'date_from': start_date.strftime('%Y-%m-%d'),
        'date_to': end_date.strftime('%Y-%m-%d'),
        'limit': 100
    }

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        return render_template('stocks.html', records=data.get('data', []))
    else:
        return render_template('error.html', error=response.text)

# 错误处理
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error="页面未找到！"), 404

if __name__ == '__main__':
    app.run(port=10000, host='0.0.0.0', debug=True)
