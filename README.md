# 🌟 Daily Fun Message Badge

Get a cute, quirky, and uplifting message on your GitHub profile every day!
auto-generates a daily message badge from `Fun_Daily_Messages_365.csv` using GitHub Actions (`.github/workflows/daily-badge.yml`)

---

## 💖 How to Use

1. Fork this repo.
2. Enable GitHub Actions in your fork.
3. Add this badge to your GitHub README:

```markdown
![Daily Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/YOUR_USERNAME/daily-badge/main/badge.json&style=for-the-badge)
```

Replace `YOUR_USERNAME` with your GitHub username.

4. 🕒 Optional: Customize timezone
To change when your daily message updates, create a file named `timezone.txt` and paste in a timezone from [this list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), e.g. `Australia/Sydney`



---

## 🔄 How It Works

- `Fun_Daily_Messages_365.csv` contains 365 fun & themed daily messages
- GitHub Action runs every midnight UTC to update `badge.json`
- That JSON powers the badge via Shields.io's `endpoint` style

You can customize the CSV to add your own themed list (e.g. sarcastic, mindful, etc.).

Made with ❤️ by in-c0