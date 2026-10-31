# Python Catalog & TON Payment-Link Starter

A Python prototype for rendering a sample digital catalog and TON payment links.

**Status: development starter / prototype.** Read the scope before integrating.

## Included

- Formats product names and example prices as Markdown.
- Builds URL-encoded TON payment links with exact nanoTON validation.

## Scope and limitations

- No running Telegram bot, AI recommendations, payment verification or order fulfillment.
- Wallet addresses in CONFIG are examples from the original author; configure your own before adapting this code.
- config.example.json is a reference; the script does not load it.

## Quick start

Python 3.10+; run from the repository directory.

```sh
python bot.py
```

## Validation

```sh
python -m unittest discover -s tests -v
```

Unit tests exercise formatting, amount validation and memo encoding. No payment is sent.

## Repository map

- `bot.py` — implementation.
- `tests/` — current checks and regression tests.
- [CHANGELOG.md](CHANGELOG.md) — changes and verification limits.
- [CONTRIBUTING.md](CONTRIBUTING.md) — issue and change guidelines.

## Downloads and usage terms

[Repository releases](https://github.com/Kirilka4345/telegram-crypto-shop-ai-bot/releases) contain historical snapshots; use the current source for the documented fixes.
No LICENSE file is present. Earlier MIT badges and commercial-license claims did not establish usable license terms. License terms require clarification before redistribution.

## Questions

For reproducible technical issues, use [GitHub Issues](https://github.com/Kirilka4345/telegram-crypto-shop-ai-bot/issues). Include the commit, runtime version, expected result and minimal reproduction. Never include tokens, cookies or customer data.
