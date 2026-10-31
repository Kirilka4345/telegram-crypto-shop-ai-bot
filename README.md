# ⚡ telegram-crypto-shop-ai-bot

> **Autonomous Telegram Digital Storefront & Multi-Chain Crypto Checkout Bot in Python (TON, USDT TRC-20, EVM & Solana).**

[![Latest Release](https://img.shields.io/github/v/release/Kirilka4345/telegram-crypto-shop-ai-bot?style=for-the-badge&logo=github&color=success)](https://github.com/Kirilka4345/telegram-crypto-shop-ai-bot/releases/latest)
[![Download Zip](https://img.shields.io/badge/Download_v1.0.0-ZIP-blue?style=for-the-badge&logo=zip)](https://github.com/Kirilka4345/telegram-crypto-shop-ai-bot/releases/download/v1.0.0/Telegram-Crypto-Shop-Bot-v1.0.zip)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 🚀 Overview

**telegram-crypto-shop-ai-bot** is a production-tested, lightweight boilerplate designed to sell digital licenses, software access tokens, downloadable assets, and premium community memberships directly inside Telegram with zero transaction fees from third-party payment gateways.

### 💎 Key Features
- **Direct Crypto Settlement:** Accept payments directly to self-custody wallets without Stripe, PayPal, or middleman merchant bans.
- **Tonkeeper 1-Click Payments:** Automatically generates native `ton://transfer` deep links with memo payload for instant mobile checkout.
- **Multi-Chain Wallet Integration:** Supports TON, USDT (TRC-20), EVM (Ethereum / Base / Polygon / Arbitrum), and Solana.
- **Modular Digital Catalog:** Define products, pricing, and automated delivery fulfillment in a clean JSON configuration.
- **Zero Heavy Dependencies:** Lightweight Python architecture easily deployable to a $3/mo Linux VPS or Docker container.

---

## ⚡ Quickstart

### 1. Installation
Clone the repository or [download the release package](https://github.com/Kirilka4345/telegram-crypto-shop-ai-bot/releases/download/v1.0.0/Telegram-Crypto-Shop-Bot-v1.0.zip):

```bash
git clone https://github.com/Kirilka4345/telegram-crypto-shop-ai-bot.git
cd telegram-crypto-shop-ai-bot
pip install -r requirements.txt
```

### 2. Configuration
Copy `config.example.json` and add your bot token from [@BotFather](https://t.me/BotFather) along with your receiving wallets:

```json
{
  "bot_token": "YOUR_TELEGRAM_BOT_TOKEN",
  "wallets": {
    "TON": "UQCwrgVAYHvlJe87-eOAK01ZzMW42E17YnbCyWPPkKeLhEpP",
    "USDT_TRC20": "TXCYzTR3Br4MuWXUnGRvpA3EaYC7iyydYj",
    "EVM": "0x12f0a957bd351492252aac81198edba4c5a56790",
    "SOLANA": "2N9dzxxt3AQRfN52FAN4W3VXvVz1aCcfXdGgwi7sHaiD8"
  }
}
```

### 3. Run
```bash
python bot.py
# or double-click START.bat on Windows
```

---

## 💼 Custom Telegram Bot Development & Freelance Orders

Need a full-featured automated sales funnel, VIP subscription bot with Telegram Stars integration, or custom CRM sync?

I develop turnkey Telegram bots:
- **Use Cases:** Digital product delivery, paid channel subscription gates, booking systems, crypto payment verifiers.
- **Integrations:** SQLite / PostgreSQL, Google Sheets, Webhooks, Telegram Stars, Crypto Pay API.
- **Deployment:** Deployment setup on Ubuntu VPS with systemd daemon auto-restart.

### 📩 Contact & Inquiries
- **GitHub:** [@Kirilka4345](https://github.com/Kirilka4345)
- **Direct Crypto Licensing ($15 – $49):**
  - **TON:** `UQCwrgVAYHvlJe87-eOAK01ZzMW42E17YnbCyWPPkKeLhEpP`
  - **USDT (TRC-20):** `TXCYzTR3Br4MuWXUnGRvpA3EaYC7iyydYj`
  - **EVM (Base / ETH):** `0x12f0a957bd351492252aac81198edba4c5a56790`
