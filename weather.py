"""Mini Test 2 - Prakiraan cuaca Jakarta 5 hari ke depan (Stamps)

Memakai endpoint gratis OpenWeatherMap: /data/2.5/forecast (data per 3 jam, 5 hari).
Satu suhu per hari diambil dari data yang paling dekat dengan pukul 12:00 waktu Jakarta.

API key TIDAK disimpan di source code. Set dulu environment variable:
    export OPENWEATHER_API_KEY=xxxxxxxx        (Linux/macOS)
    set OPENWEATHER_API_KEY=xxxxxxxx           (Windows CMD)
lalu jalankan:
    python weather.py
"""

import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

API_URL = "https://api.openweathermap.org/data/2.5/forecast"
CITY = "Jakarta,ID"
DAYS = 5


def fetch_forecast(api_key: str) -> dict:
    params = urllib.parse.urlencode({"q": CITY, "units": "metric", "appid": api_key})
    with urllib.request.urlopen(f"{API_URL}?{params}", timeout=15) as resp:
        return json.load(resp)


def daily_temperatures(data: dict, days: int = DAYS):
    """Kembalikan list (tanggal, suhu) — satu suhu per hari, diambil dari jam terdekat ke 12:00 lokal."""
    tz = timezone(timedelta(seconds=data.get("city", {}).get("timezone", 7 * 3600)))
    picked = {}
    for item in data["list"]:
        local = datetime.fromtimestamp(item["dt"], tz)
        distance = abs(local.hour - 12)
        day = local.date()
        if day not in picked or distance < picked[day][0]:
            picked[day] = (distance, item["main"]["temp"])

    today = datetime.now(tz).date()
    upcoming = sorted(d for d in picked if d > today)  # 5 hari ke depan (mulai besok)
    if len(upcoming) < days:  # jika data besok+ kurang dari 5 hari, sertakan hari ini
        upcoming = sorted(picked)
    return [(d, picked[d][1]) for d in upcoming[:days]]


def main() -> None:
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        sys.exit("Error: set environment variable OPENWEATHER_API_KEY terlebih dahulu.")

    try:
        data = fetch_forecast(api_key)
    except Exception as exc:  # noqa: BLE001
        sys.exit(f"Gagal mengambil data cuaca: {exc}")

    print("Weather Forecast:")
    for day, temp in daily_temperatures(data):
        print(f"{day.strftime('%a, %d %b %Y')}: {temp:.2f}°C")


if __name__ == "__main__":
    main()
