import os
from platform import system
from typing import Dict, List, Union


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


def print_pomodoros_table(data: List[List[str]], headers: List[str]) -> str:
    col_widths = [
        max(len(str(item)) for item in col) for col in zip(*([headers] + data))
    ]
    row_format = f"  {prPurple("│")} ".join([f"{{:<{width}}}" for width in col_widths])
    table_str = ""
    header_line = row_format.format(*headers)
    separator = "─".join(["─" * (width + 2) for width in col_widths])
    table_str += prPurple(header_line) + "\n"
    table_str += prPurple(separator) + "\n"
    for row in data:
        table_str += row_format.format(*row) + "\n"
    return table_str


def print_stats_from_dict(stats: Dict[str, Union[str, int, float, List[str]]]) -> str:
    max_key_len = max(len(str(key)) for key in stats.keys())

    def get_value_length(v):
        return len(", ".join(v)) if isinstance(v, list) else len(str(v))

    max_value_len = max(get_value_length(v) for v in stats.values())
    table_lines = []
    separator = "─" * (max_key_len + max_value_len + 5)
    table_lines.append(prCyan(" GENERAL STATISTICS ".center(len(separator), "─")))

    for key, value in stats.items():
        formatted_value = ", ".join(value) if isinstance(value, list) else str(value)
        key_part = f"{key.ljust(max_key_len)}"
        table_lines.append(f"{key_part} {prCyan("│")} {formatted_value}")
    table_lines.append(prCyan(separator))
    return "\n".join(table_lines)
