from pomodoro.utils.format import format_time, prRed
from pomodoro.log import log_a_pomodoro
import time
import sys
import os


def countdown(minutes, message, action="focus", tag=None):
    seconds = minutes * 60
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
    if action=="focus":
        log_a_pomodoro(minutes, message, tag)
    # El parámetro -w no funciona en linux-mint
    # os.system('notify-send -w -t 15000 "' + message + ' completado!"&')
    os.system('notify-send -u critical -t 15000 "' + message + ' completado!"&')
    return True
