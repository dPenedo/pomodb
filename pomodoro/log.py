from datetime import datetime
from pomodoro.utils.constants import LOG_FILE


def log_a_pomodoro(minutes: int, message: str, tag: str | None):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        _ = file.write(
            f"\ndatetime:{datetime.now()} | minutes: {minutes} | message: {message} | tag:{tag}"
        )
