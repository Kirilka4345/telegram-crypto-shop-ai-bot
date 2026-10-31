# -*- coding: utf-8 -*-
"""Catalog and TON payment-link formatting prototype; no payment verification."""
from decimal import Decimal, InvalidOperation
from urllib.parse import urlencode
import os
import sys
import json
import logging
from typing import Dict, Any

if hasattr(sys.stdout, "reconfigure"):
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
        {"id": "vip_sniper", "name": "Example digital product A", "price_ton": 1.0, "price_usdt": 5.2},
        {"id": "ui_kit", "name": "Example digital product B", "price_ton": 2.5, "price_usdt": 12.99},
        {"id": "stealth_scraper", "name": "Python Playwright Stealth Scraper Kit", "price_ton": 3.0, "price_usdt": 15.0}
    ]
}

def generate_tonkeeper_url(amount_ton: float, comment: str) -> str:
    wallet = CONFIG["WALLETS"]["TON"]
    try:
        value = Decimal(str(amount_ton)) * Decimal(1000000000)
        if not value.is_finite() or value <= 0 or value != value.to_integral_value():
            raise ValueError("Amount must be positive, finite and exact to nanoTON")
        nano = int(value)
    except InvalidOperation as exc:
        raise ValueError("Invalid TON amount") from exc
    return f"ton://transfer/{wallet}?" + urlencode({"amount": nano, "text": comment})

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
