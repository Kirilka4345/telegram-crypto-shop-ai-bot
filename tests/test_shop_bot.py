# -*- coding: utf-8 -*-
"""Unit tests for Telegram Crypto Shop AI Bot."""
import unittest
import sys
from pathlib import Path

# Add parent directory to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from bot import CONFIG, generate_tonkeeper_url, get_catalog_markdown

class TestCryptoShopBot(unittest.TestCase):
    def test_tonkeeper_url_generation(self):
        """Test Tonkeeper deep link generation and nanoTON precision."""
        url = generate_tonkeeper_url(1.5, "order_123")
        self.assertTrue(url.startswith("ton://transfer/"))
        self.assertIn("amount=1500000000", url)
        self.assertIn("text=order_123", url)
        self.assertIn(CONFIG["WALLETS"]["TON"], url)

    def test_wallets_configuration(self):
        """Verify all accepted payment chain wallets exist and match address specifications."""
        wallets = CONFIG.get("WALLETS", {})
        self.assertIn("TON", wallets)
        self.assertIn("USDT_TRC20", wallets)
        self.assertIn("EVM", wallets)
        self.assertIn("SOLANA", wallets)
        self.assertTrue(wallets["TON"].startswith("UQ"))
        self.assertTrue(wallets["USDT_TRC20"].startswith("T"))
        self.assertTrue(wallets["EVM"].startswith("0x"))

    def test_products_catalog(self):
        """Verify product schema and minimum requirements."""
        products = CONFIG.get("PRODUCTS", [])
        self.assertGreaterEqual(len(products), 1)
        for p in products:
            self.assertIn("id", p)
            self.assertIn("name", p)
            self.assertIn("price_ton", p)
            self.assertIn("price_usdt", p)
            self.assertGreater(p["price_ton"], 0)
            self.assertGreater(p["price_usdt"], 0)

    def test_catalog_markdown(self):
        """Verify formatted markdown contains Tonkeeper deep links and product info."""
        md = get_catalog_markdown()
        self.assertIn("Tonkeeper", md)
        self.assertIn("Direct USDT", md)
        for p in CONFIG["PRODUCTS"]:
            self.assertIn(p["name"], md)

if __name__ == "__main__":
    unittest.main()
