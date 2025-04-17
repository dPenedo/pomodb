from pomodoro.utils.format import format_time, prRed
from pomodoro.log import log_a_pomodoro
import time
import sys
import os


def countdown(minutes, message, action="focus", tag=None):
    # WARN: 60
    seconds = minutes * 2
    print(f"{message} started")
    if tag is None:
        print(f"\rGet {action} for:")
    else:
        print(f"\rGet {action} on {prRed(tag)} for:")
    for remaining in range(seconds, 0, -1):
        sys.stdout.write(f"\r{format_time(remaining)}s")
        sys.stdout.flush()
        time.sleep(1)

    print(f"{message} finished")
    log_a_pomodoro(minutes, message, tag)
    os.system('notify-send -w -t 15000 "' + message + ' completado!"&')
    return True
