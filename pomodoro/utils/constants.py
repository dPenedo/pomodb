from typing import TypedDict


class PomodoroConfig(TypedDict):
    minutes: int
    text: str
    action: str


# For debug: changee 25 and 5
WORK: PomodoroConfig = {"minutes": 25, "text": "🍅 Pomodoro", "action": "focus"}
REST: PomodoroConfig = {"minutes": 5, "text": "󱕮  Rest", "action": "rest"}
LOG_FILE = "log.txt"

DB_FILENAME = "pomodoros.db"
POMODORO_TABLE = "pomodoros"
