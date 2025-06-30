from pomodoro.db.queries import log_a_pomodoro
from pomodoro.utils.format import format_time, prRed
import time
import sys
import os


def countdown(
    minutes: int, message: str, action: str = "focus", tag: str | None = None
):
    seconds = minutes * 60
    print(f"{message} started")
    if tag is None:
        print(f"\rGet {action} for:")
    else:
        print(f"\rGet {action} on {prRed(tag)} for:")
    for remaining in range(seconds, 0, -1):
        _ = sys.stdout.write(f"\r{format_time(remaining)}s")
        _ = sys.stdout.flush()
        time.sleep(1)

    print(f"{message} finished")
    if action == "focus":
        log_a_pomodoro(minutes, message, tag)
    # WARN: El parámetro -w no funciona en linux-mint
    # os.system('notify-send -w -t 15000 "' + message + ' completed!"&')
    _ = os.system('notify-send -u critical -t 15000 "' + message + ' completed!"&')
    return True
