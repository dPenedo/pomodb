from pomodoro.db.queries import get_sum_of_minutes
from pomodoro.utils.format import print_pomodoros_table, print_stats_from_dict


def get_stats() -> str:
    headers = ["Fecha", "Pomodoros", "Duración"]
    data = [
        ["2023-10-01", "4", "100 min"],
        ["2023-10-02", "5", "125 min"],
    ]

    table = print_pomodoros_table(data, headers)  # Ahora devuelve un string

    general_stats = {
        "Total of Pomodoros": get_sum_of_minutes(9),
        "Total of Pomodoros of This Week": 12,
        "Tags of This Week": ["work", "study"],
        "Average of Pomodoros this Week": "5 días",
    }

    stats_text = f"""
{"-"*50}STATISTICS{"-"*50}
{print_stats_from_dict(general_stats)}
{"-"*50}
{table}

    """
    return stats_text
