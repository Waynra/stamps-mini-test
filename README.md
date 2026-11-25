# Stamps – Mini Test (Developer)

Bahasa: Python 3 (tanpa library tambahan).

## 1. Small Program
```bash
python foobar.py
```

## 2. Weather Forecast Jakarta (5 hari)
API key tidak disimpan di source code — dibaca dari environment variable.
```bash
export OPENWEATHER_API_KEY=<api_key_anda>   # Windows: set OPENWEATHER_API_KEY=<api_key_anda>
python weather.py
```
Menggunakan endpoint gratis `/data/2.5/forecast`; satu suhu per hari diambil dari data terdekat pukul 12:00 WIB.
