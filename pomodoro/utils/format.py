import os
from platform import system


def format_time(seconds: int) -> str:
    return f"{seconds // 60:0d}:{seconds % 60:02d}"


def clear_screen() -> None:
    _ = os.system("cls" if system() == "Windows" else "clear")


def red(skk: str) -> str:
    return "\033[91m{}\033[00m".format(skk)


def cyan(skk: str) -> str:
    return "\033[96m{}\033[00m".format(skk)


def purple(skk: str) -> str:
    return "\033[95m{}\033[00m".format(skk)


def get_pomodoros_table(
    data: list[list[str]], headers: list[str], title: str = "LAST 20 POMODOROS"
) -> str:
    col_widths = [
        max(len(str(item)) for item in col) for col in zip(*([headers] + data))
    ]
    row_format = f"  {purple('│')} ".join([f"{{:<{width}}}" for width in col_widths])
    total_width = sum(col_widths) + (
        3 * (len(col_widths) - 1)
    )  # 3 por los separadores " │ "
    table_lines = []
    separator = "─" * total_width
    table_lines.append(purple(f" {title} ".center(total_width, "─")))
    header_line = row_format.format(*headers)
    table_lines.append(purple(header_line))
    table_lines.append(purple(separator))
    for row in data:
        table_lines.append(row_format.format(*row))
    table_lines.append(purple(separator))
    return "\n".join(table_lines)


def get_stats_from_dict(stats: dict[str, str | int | float | list[str]]) -> str:
    max_key_len = max(len(str(key)) for key in stats.keys())

    def get_value_length(v):
        return len(", ".join(v)) if isinstance(v, list) else len(str(v))

    max_value_len = max(get_value_length(v) for v in stats.values())
    table_lines = []
    separator = "─" * (max_key_len + max_value_len + 5)
    table_lines.append(cyan(" GENERAL STATISTICS ".center(len(separator), "─")))

    for key, value in stats.items():
        formatted_value = ", ".join(value) if isinstance(value, list) else str(value)
        key_part = f"{key.ljust(max_key_len)}"
        table_lines.append(f"{key_part} {cyan('│')} {formatted_value}")
    table_lines.append(cyan(separator))
    return "\n".join(table_lines)
