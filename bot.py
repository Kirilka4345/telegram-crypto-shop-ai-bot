# -*- coding: utf-8 -*-
"""Standalone Telegram Crypto Shop Bot with Tonkeeper & Multi-chain Checkout."""
import os
import sys
import json
import logging
from typing import Dict, Any

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

CONFIG = {
    "BOT_TOKEN": os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_FROM_BOTFATHER"),
    "WALLETS": {
        "TON": "UQCwrgVAYHvlJe87-eOAK01ZzMW42E17YnbCyWPPkKeLhEpP",
        "USDT_TRC20": "TXCYzTR3Br4MuWXUnGRvpA3EaYC7iyydYj",
        "EVM": "0x12f0a957bd351492252aac81198edba4c5a56790",
        "SOLANA": "2N9dzxxt3AQRfN52FAN4W3VXvVz1aCcfXdGgwi7sHaiD8"
    },
    "PRODUCTS": [
        {"id": "vip_sniper", "name": "TON Gifts 0-Second VIP Sniper License", "price_ton": 1.0, "price_usdt": 5.2},
        {"id": "ui_kit", "name": "Dark Fantasy 2D UI & Icon Kit for Unity/Roblox", "price_ton": 2.5, "price_usdt": 12.99},
        {"id": "stealth_scraper", "name": "Python Playwright Stealth Scraper Kit", "price_ton": 3.0, "price_usdt": 15.0}
    ]
}

def generate_tonkeeper_url(amount_ton: float, comment: str) -> str:
    wallet = CONFIG["WALLETS"]["TON"]
    nano = int(amount_ton * 1e9)
    return f"ton://transfer/{wallet}?amount={nano}&text={comment}"

def get_catalog_markdown() -> str:
    lines = ["🛍️ **Crypto Digital Goods Store**\n"]
    for p in CONFIG["PRODUCTS"]:
        lines.append(f"• **{p['name']}**")
        lines.append(f"  💰 Price: `{p['price_ton']} TON` or `${p['price_usdt']} USDT`")
        lines.append(f"  👉 Quick Pay: [Pay via Tonkeeper]({generate_tonkeeper_url(p['price_ton'], p['id'])})\n")
    lines.append(f"💵 **Direct USDT (TRC-20):** `{CONFIG['WALLETS']['USDT_TRC20']}`")
    lines.append(f"🌐 **EVM (Base/Polygon/ETH):** `{CONFIG['WALLETS']['EVM']}`")
    lines.append(f"⚡ **Solana (SOL):** `{CONFIG['WALLETS']['SOLANA']}`")
    return "\n".join(lines)

if __name__ == "__main__":
    print("Catalog Preview:\n")
    print(get_catalog_markdown())

