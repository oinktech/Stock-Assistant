
# 股票助手 (Stock Assistant)

[![Flask](https://img.shields.io/badge/Flask-v2.2.2-blue.svg)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-v3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 語言選擇 / Language Selection

<div style="text-align:center;">
    <a href="#功能"><img src="https://openmoji.org/data/color/svg/1F1F9-1F1FC.svg" alt="繁體中文" width="40" /></a>
    <a href="#features"><img src="https://openmoji.org/data/color/svg/1F1FA-1F1F8.svg" alt="English" width="40" /></a>
</div>

---

## 內容 / Table of Contents

- [功能](#功能)
- [安裝](#安裝)
- [使用](#使用)
- [示範](#示範)
- [貢獻](#貢獻)
- [許可證](#許可證)

---

## 功能 / Features

- 查看所有股票數據 / View all stock data
- 查詢特定股票的詳情 / Query details of a specific stock
- 搜索股票功能 / Search stocks functionality
- 多語言支持（繁體中文和英文）/ Multi-language support (Traditional Chinese and English)
- 數據圖表顯示 / Data visualization with charts
- 錯誤處理和提示 / Error handling and notifications

---

## 安裝 / Installation

請確保您已安裝 Python 3 和 pip。

1. 克隆這個儲存庫：

   ```bash
   git clone https://github.com/oinktech/stock_app.git
   cd stock_app
   ```

2. 安裝依賴：

   ```bash
   pip install -r requirements.txt
   ```

---

## 使用 / Usage

運行以下命令啟動應用：

```bash
python app.py
```

然後在瀏覽器中訪問 `http://127.0.0.1:10000`。

Run the following command to start the application:

```bash
python app.py
```

Then visit `http://127.0.0.1:10000` in your browser.

---

## 示範 / Demo

### 頁面截圖 / Screenshots

![主頁](https://via.placeholder.com/800x400.png?text=主頁+Screenshot)  
![股票記錄](https://via.placeholder.com/800x400.png?text=股票記錄+Screenshot)

### 動畫效果 / Animation Effects

```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.container {
  animation: fadeIn 0.5s ease-in-out;
}
```

---

## 貢獻 / Contributing

如果您想為此項目做出貢獻，請遵循以下步驟：

1. Fork 此儲存庫
2. 創建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 創建一個新的 Pull Request

---

## 許可證 / License

此項目使用 MIT 許可證 - 詳見 [LICENSE](LICENSE) 文件。

---

### 附加信息 / Additional Information

- **技術棧**: Flask, SQLAlchemy, HTML, CSS, JavaScript
- **數據來源**: 股票市場 API
- **支持的瀏覽器**: Chrome, Firefox, Safari

