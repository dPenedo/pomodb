from typing import TypedDict


class PomodoroConfig(TypedDict):
    minutes: int
    text: str
    action: str


WORK: PomodoroConfig = {"minutes": 25, "text": "🍅 Pomodoro", "action": "focus"}
REST: PomodoroConfig = {"minutes": 5, "text": "󱕮  Rest", "action": "rest"}
LOG_FILE = "log.txt"
