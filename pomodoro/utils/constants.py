from typing import TypedDict


class PomodoroConfig(TypedDict):
    minutes: int
    text: str
    action: str


# WARN::changee to 25 and 5!
WORK: PomodoroConfig = {"minutes": 1, "text": "🍅 Pomodoro", "action": "focus"}
REST: PomodoroConfig = {"minutes": 1, "text": "󱕮  Rest", "action": "rest"}
LOG_FILE = "log.txt"

DB_FILENAME = "pomodoros.db"
POMODORO_TABLE = "pomodoros"
