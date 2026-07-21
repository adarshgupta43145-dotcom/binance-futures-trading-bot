# Binance Futures Testnet Trading Bot

A modular Python 3.11+ application for placing **BUY/SELL MARKET and LIMIT orders** on the **Binance Futures Testnet (USDT-M)** using the `python-binance` library.

---

## Features

- ✅ Supports MARKET and LIMIT orders
- ✅ Supports BUY and SELL orders
- ✅ Command-line interface using `argparse`
- ✅ Input validation
- ✅ Error handling
- ✅ Logging to `logs/trading.log`
- ✅ Reads API credentials from `.env`
- ✅ Rich CLI output using `rich`
- ✅ Modular project structure

---

## Project Structure

```text
TRADING_BOT/
│── screenshots/
│   ├── market_order.png
│   └── limit_order.png
│── logs/
│── .env.example
│── .gitignore
│── cli.py
│── client.py
│── logging_config.py
│── orders.py
│── README.md
│── requirements.txt
│── validators.py
```

---

## Installation

### 1. Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

```bash
copy .env.example .env
```

Open `.env` and add:

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_API_SECRET
```

---

## Usage

### Market Buy

```bash
python cli.py buy BTCUSDT --quantity 0.001
```

### Market Sell

```bash
python cli.py sell BTCUSDT --quantity 0.001
```

### Limit Buy

```bash
python cli.py buy BTCUSDT --quantity 0.001 --order-type LIMIT --price 68000
```

### Limit Sell

```bash
python cli.py sell BTCUSDT --quantity 0.001 --order-type LIMIT --price 69000
```

---

## Screenshots

### Market Order

![Market Order](screenshots/market_order.png)

---

### Limit Order

![Limit Order](screenshots/limit_order.png)

---

## Logging

The application stores logs in:

```text
logs/trading.log
```

Logs include:

- API requests
- Order responses
- Validation errors
- Exceptions

---

## Tech Stack

- Python 3.11+
- python-binance
- python-dotenv
- rich
- argparse

---

## Notes

- Uses **Binance Futures Testnet (USDT-M)** only.
- Requires valid Testnet API credentials.
- Designed for educational and evaluation purposes.