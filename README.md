# 股票助手 (Stock Helper)
# [線上體驗版 (Live Demo)](https://stock-assistant-4rrt.onrender.com)
![Logo](https://openmoji.org/data/color/svg/1F4B1.svg)

## 語言選擇 / Language Selection
- [繁體中文](#繁體中文)
- [English](#english)

---

## 繁體中文

### 介紹

**股票助手** 是一個功能強大的股市查詢應用，利用 Flask 框架提供即時的股票數據和分析。無論你是專業投資者還是股市新手，這個應用都能幫助你更好地了解市場動態。

### 主要功能

- **即時股票數據**: 獲取最新的股票報價及市場變化。
- **詳細股票資訊**: 每隻股票都有專屬頁面，顯示其詳細資料，包括歷史表現和技術指標。
- **搜尋與篩選功能**: 快速查找股票，支持按代碼或名稱篩選。
- **響應式設計**: 支持桌面及移動設備，流暢使用體驗。
- **數據可視化**: 內建圖表顯示股票走勢，讓數據一目瞭然。
- **友好的動畫效果**: 提升用戶互動體驗。

### 安裝指南

1. **克隆儲存庫**：

   ```bash
   git clone https://github.com/oinktech/stock_app.git
   cd stock_app
   ```

2. **安裝依賴**：

   確保你已安裝 Python 3 和 pip，然後運行以下命令：

   ```bash
   pip install -r requirements.txt
   ```

### 啟動應用

運行以下命令啟動應用：

```bash
python app.py
```

然後在瀏覽器中訪問 `http://127.0.0.1:10000` 開始使用。

### 使用指南

1. **首頁展示**: 進入應用後，首頁會列出所有股票的最新數據。
2. **搜尋股票**: 使用搜尋框快速查找特定股票代碼或名稱。
3. **查看詳情**: 點擊任何股票代碼可進入詳細資訊頁面，查看其歷史表現和最新數據。

### 截圖

![Stocks Page](https://example.com/stocks-page-screenshot.png)

### 數據可視化

使用 Chart.js 库生成的股票走勢圖：

```html
<canvas id="stockChart" width="400" height="200"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    var ctx = document.getElementById('stockChart').getContext('2d');
    var stockChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June'],
            datasets: [{
                label: 'Stock Price',
                data: [65, 59, 80, 81, 56, 55],
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
</script>
```

### 動畫效果

本應用具備優雅的 CSS 動畫，提升用戶交互體驗。以下是一個示例動畫：

```css
@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

.fade-in {
    animation: fadeIn 1s ease-in;
}
```

將 `.fade-in` 類添加到你的 HTML 元素中，讓它們在進入視窗時淡入顯示。

---

## English

### Introduction

**Stock Helper** is a powerful stock query application built on the Flask framework that provides real-time stock data and analysis. Whether you're a seasoned investor or new to the stock market, this application helps you stay informed about market trends.

### Key Features

- **Real-time Stock Data**: Get the latest stock quotes and market movements.
- **Detailed Stock Information**: Each stock has a dedicated page displaying comprehensive details, including historical performance and technical indicators.
- **Search and Filter Functionality**: Quickly find stocks by symbol or name with advanced filtering options.
- **Responsive Design**: Fully compatible with both desktop and mobile devices for a smooth user experience.
- **Data Visualization**: Built-in charts show stock trends, making data easy to understand.
- **Friendly Animations**: Enhance user interaction experience.

### Installation Guide

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/oinktech/stock_app.git
   cd stock_app
   ```

2. **Install Dependencies**:

   Ensure you have Python 3 and pip installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the application with the following command:

```bash
python app.py
```

Then visit `http://127.0.0.1:10000` in your browser to start using the app.

### Usage Guide

1. **Homepage Display**: Upon entering the app, the homepage lists all stocks with their latest data.
2. **Search for Stocks**: Use the search box to quickly find specific stock symbols or names.
3. **View Details**: Click on any stock symbol to access detailed information, including historical performance and latest data.

### Screenshots

![Stocks Page](https://example.com/stocks-page-screenshot.png)

### Data Visualization

Using Chart.js to generate stock trend charts:

```html
<canvas id="stockChart" width="400" height="200"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    var ctx = document.getElementById('stockChart').getContext('2d');
    var stockChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June'],
            datasets: [{
                label: 'Stock Price',
                data: [65, 59, 80, 81, 56, 55],
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
</script>
```

### Animations

The application features elegant CSS animations to enhance user interactions. Below is an example animation:

```css
@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

.fade-in {
    animation: fadeIn 1s ease-in;
}
```

Add the `.fade-in` class to your HTML elements to make them fade in when they enter the viewport.

---

## 開發者 (Developer)

- **OinkTech**: [GitHub](https://github.com/oinktech)
- **聯繫我們 (Contact Us)**: oinktech2024@gmail.com
