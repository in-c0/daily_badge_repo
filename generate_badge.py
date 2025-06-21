import pandas as pd
from datetime import datetime
import json
import pytz
import os

# ─── Load Timezone ─────────────────────────────────────────────
DEFAULT_TZ = "UTC"
timezone_path = "timezone.txt"

if os.path.exists(timezone_path):
    try:
        with open(timezone_path, "r") as f:
            user_tz = f.read().strip()
            tz = pytz.timezone(user_tz)
    except Exception:
        tz = pytz.timezone(DEFAULT_TZ)
else:
    tz = pytz.timezone(DEFAULT_TZ)

# ─── Determine Today (User's Local Time) ───────────────────────
today = datetime.now(tz)
month = today.strftime("%B")
day = today.day

# ─── Load Messages ─────────────────────────────────────────────
df = pd.read_csv("What_Day_365.csv")

try:
    today_message = df[(df["Day"] == f"{month} {day}")]["Message"].values[0]
except IndexError:
    today_message = "You're amazing!"

# ─── Create Badge JSON ─────────────────────────────────────────
badge = {
    "schemaVersion": 1,
    "label": "Today is ... ",
    "message": today_message,
    "color": "pink"
}

with open("badge.json", "w") as f:
    json.dump(badge, f)

print(f"[{today.strftime('%Y-%m-%d')}] Generated badge in timezone: {tz}")
