
# Card Schemer V1.0

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Terminal Tool](https://img.shields.io/badge/CLI-Tool-orange)

A simple card validator that checks **Luhn validity** and fetches **BIN metadata** instantly.

## 🚀 Features
- 💳 Luhn Algorithm check  
- 🌍 BIN Lookup (brand, bank, country, etc.)  

## 📦 Install
```
pip install -r requirements.txt
```

## ▶️ Run
Interactive:
```
python card_schemer.py
```

One‑shot:
```
python card_schemer.py 4111111111111111
```

## 📌 Notes
- BIN API used: `https://api.juspay.in/cardbins/{bin}`
- Replace with your preferred provider if needed.

## 👑 Developer
**777AMANAT**

## 📄 License
MIT
