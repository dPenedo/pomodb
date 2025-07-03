from pomodoro.db.queries import (
    get_average_of_days,
    get_list_of_pomodoros,
    get_list_of_tags,
    get_sum_of_pomodoros,
)
from pomodoro.utils.format import print_pomodoros_table, print_stats_from_dict


def get_stats() -> str:
    headers = ["Date", "Duration", "Tag"]
    table = print_pomodoros_table(get_list_of_pomodoros(7, 20), headers)

    general_stats = {
        "Total of Pomodoros": get_sum_of_pomodoros(-1),
        "Total of Pomodoros of Today": get_sum_of_pomodoros(1),
        "Tags of Pomodoros of Last 7 Days": get_list_of_tags(7),
        "Tags of Pomodoros of Today": get_list_of_tags(1),
        "Average of Pomodoros this Week": get_average_of_days(7),
    }

    stats_text = f"""
{print_stats_from_dict(general_stats)}
{table}

    """
    return stats_text
