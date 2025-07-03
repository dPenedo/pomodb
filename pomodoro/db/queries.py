from typing import List
from pomodoro.db.db_utils import execute_non_query, execute_query
from pomodoro.db.models import get_db_connection
from pomodoro.utils.constants import POMODORO_TABLE


def log_a_pomodoro(minutes: int, message: str, tag: str | None):
    query = f"""
        INSERT INTO {POMODORO_TABLE} ( minutes, message, tag)
        VALUES (?, ?, ?)
    """
    success = execute_non_query(
        query,
        (
            minutes,
            message,
            tag,
        ),
    )
    if success:
        print("Pomodo registered")


def get_sum_of_pomodoros(days: int) -> int:
    interval = f"-{9999 if days == -1 else days} days"
    query = f"""
        SELECT COUNT(*)
        FROM {POMODORO_TABLE}
        WHERE created_at >= (SELECT DATETIME('now', ?))
    """
    rows = execute_query(query, (interval,))
    return rows[0][0] if rows else 0


def get_list_of_pomodoros(days: int, limit: int) -> List[str]:
    interval = f"-{9999 if days == -1 else days} days"
    list_of_pomodoros = ["There are no pomodoros yet"]
    query = f"""
        SELECT *
        FROM {POMODORO_TABLE}
        WHERE created_at >= (SELECT DATETIME('now', ?))
        ORDER  BY created_at DESC
        LIMIT ?
    """
    rows = execute_query(
        query,
        (
            interval,
            limit,
        ),
    )
    if rows:
        list_of_pomodoros.clear()
    for e in rows:
        pomodoro_list = []
        pomodoro_list.append(str(e[1]))  # Date
        pomodoro_list.append(str(e[2]))  # Duration
        pomodoro_list.append(str(e[4]))  # Tag
        list_of_pomodoros.append(pomodoro_list)

    return list_of_pomodoros


def get_list_of_tags(days: int) -> List[str]:
    interval = f"-{9999 if days == -1 else days} days"
    list_of_tags = ["There are not tags yet"]
    query = f"""
            SELECT DISTINCT tag
            FROM {POMODORO_TABLE}
            WHERE created_at >= (SELECT DATETIME('now', ?))
        """
    rows = execute_query(query, (interval,))
    if rows:
        list_of_tags.clear()
    for e in rows:
        list_of_tags.append(str(e[0]))
    return list_of_tags


def get_average_of_days(days: int) -> int:
    interval = f"-{days} days"
    average_of_tags = -1
    query = f"""
            SELECT COUNT(minutes)/ ?
            FROM {POMODORO_TABLE}
            WHERE created_at >= (SELECT DATETIME('now', ?))
        """
    average_output = execute_query(
        query,
        (
            days,
            interval,
        ),
    )
    if average_output:
        average_of_tags = int(average_output[0][0])
    return average_of_tags
