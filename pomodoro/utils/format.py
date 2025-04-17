import os
from platform import system


def format_time(seconds):
    return f"{seconds//60:0d}:{seconds%60:02d}"


def clear_screen():
    os.system("cls" if system() == "Windows" else "clear")


def prRed(skk):
    return "\033[91m {}\033[00m".format(skk)


def prCyan(skk):
    return "\033[96m{}\033[00m".format(skk)


def prPurple(skk):
    return "\033[95m{}\033[00m".format(skk)
