# 🍅 Pomodoro CLI

A lightweight, no-dependency command-line Pomodoro timer with persistent stats and desktop notifications.

---

## ✨ Features

- ⏱ Start and customize Pomodoro sessions
- 🏷 Add tags to your sessions
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
- 🏷 `tag`: Optional tag for filtering or grouping

This allows you to:

- Count sessions in a given time range
- Calculate your daily average
- List recent pomodoros with tags or notes

---

## 📁 Project Structure

├──  pomodoro
│ ├──  cli
│ │ ├──  **pycache**
│ │ ├──  commands.py
│ │ └──  parser.py
│ ├──  db
│ │ ├──  db_utils.py
│ │ ├──  models.py
│ │ └──  queries.py
│ ├──  utils
│ │ ├──  constants.py
│ │ ├──  format.py
│ │ ├──  stats.py
│ │ └──  total_time.py
│ ├──  **main**.py
│ └──  countdown.py
├──  pomodoros.db
├──  LICENSE
├──  README.md
└──  setup.py

---

## 🔔 Notifications

If you're on Linux and have `notify-send` available, you’ll get desktop notifications when each pomodoro or rest period ends. No configuration needed.

---

## License

This project is licensed under the [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
