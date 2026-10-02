from pomodoro.db.queries import insert_pomodoro
from pomodoro.utils.format import format_time, red
from pomodoro.utils.sounds import play
import time
import sys
import os


def countdown(
    minutes: int,
    work: bool,
    notifications_enabled: bool,
    tag: str | None = None,
):
    seconds = minutes * 60
    play("gong.mp3")
    message = "🍅 Pomodoro" if work else "󱕮  Rest"
    action = "focus" if work else "rest"
    print(f"{message} started")
    if tag is None:
        print(f"\rGet {action} for:")
    else:
        print(f"\rGet {action} on {red(tag)} for:")
    for remaining in range(seconds, 0, -1):
        _ = sys.stdout.write(f"\r{format_time(remaining)}s")
        _ = sys.stdout.flush()
        time.sleep(1)

    print(f"{message} finished")
    if action == "focus" and insert_pomodoro(minutes, message, tag):
        print("Pomodoro registered")
    if notifications_enabled:
        _ = os.system('notify-send -u critical -t 15000 "' + message + ' completed!"&')
    play("gong.mp3")
    return True
