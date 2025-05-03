import os
from platform import system


def format_time(seconds: int):
    return f"{seconds//60:0d}:{seconds%60:02d}"


def clear_screen():
    _ = os.system("cls" if system() == "Windows" else "clear")


def prRed(skk: str):
    return "\033[91m {}\033[00m".format(skk)


def prCyan(skk: str):
    return "\033[96m{}\033[00m".format(skk)


def prPurple(skk: str):
    return "\033[95m{}\033[00m".format(skk)
