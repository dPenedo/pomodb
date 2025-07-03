# 🍅 Pomodoro CLI

A lightweight, no-dependency command-line Pomodoro timer with persistent stats and desktop notifications.

---

## ✨ Features

- ⏱ Start and customize Pomodoro sessions
- 📌 Add tags to your sessions
- 📊 Track stats over time with SQLite
- 🔔 Sends desktop notifications on Linux when pomodoros and breaks end
- 📦 No external dependencies
- 🧼 Self-contained and easy to read

---

## 🔧 Requirements

- Python 3.10+
- SQLite (built into Python)

---

## ▶️ How to use it?

Clone the repo and run from the project root:

```bash
python -m pomodoro start             # Start a session (25 minutes)
python -m pomodoro start -n 2        # Run 2 pomodoros (default: 4)
python -m pomodoro start -t writing  # Start a session with a tag
python -m pomodoro stats             # View stats and history
python -m pomodoro help              # Show CLI help
```

## What gets saved?

Each completed pomodoro is stored in a local SQLite database with the following fields:

- 🆔 `id`: A unique identifier
- 🕒 `created_at`: Date and time when the session ended
- ⏳ `minutes`: Duration of the session
- 📝 `message`: Currently always should show "🍅 Pomodoro", in the future it could be expanded
- 📌 `tag`: Optional tag for filtering or grouping

This allows you to:

- Count sessions in a given time range
- Calculate your daily average
- List recent pomodoros with tags or notes

---

## 🔔 Notifications

If you're on Linux and have `notify-send` available, you’ll get desktop notifications when each pomodoro or rest period ends. No configuration needed.

---

## License

This project is licensed under the MIT License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
