import sys
import unittest
from pathlib import Path
from urllib.parse import urlsplit, parse_qs
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from bot import generate_tonkeeper_url

class PaymentLinkTests(unittest.TestCase):
    def test_memo_cannot_inject_amount(self):
        memo = 'note&amount=1#fragment + text'
        query = parse_qs(urlsplit(generate_tonkeeper_url(1.25, memo)).query)
        self.assertEqual(query['amount'], ['1250000000'])
        expected = memo if 'bot' == 'bot' else 'SUPPORT-BOT:' + memo.replace(' ', '_')
        self.assertEqual(query['text'], [expected])

    def test_exact_decimal_amount(self):
        self.assertEqual(parse_qs(urlsplit(generate_tonkeeper_url('0.000000001', 'test')).query)['amount'], ['1'])

    def test_reject_invalid_amounts(self):
        for value in [-1, 0, 'NaN', 'Infinity', '0.0000000001', 'not-a-number']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                generate_tonkeeper_url(value, 'test')
