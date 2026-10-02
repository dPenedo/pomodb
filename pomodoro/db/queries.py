from pomodoro.db.db_utils import execute_non_query, execute_query


def insert_pomodoro(minutes: int, message: str, tag: str | None) -> bool:
    query = """
        INSERT INTO pomodoros ( minutes, message, tag)
        VALUES (?, ?, ?)
    """
    return execute_non_query(
        query,
        (
            minutes,
            message,
            tag,
        ),
    )


def get_sum_of_pomodoros(days: int) -> int:
    interval = f"-{9999 if days == -1 else days} days"
    query = """
        SELECT COUNT(*)
        FROM pomodoros 
        WHERE created_at >= (SELECT DATETIME('now', ?))
    """
    rows = execute_query(query, (interval,))
    return rows[0][0] if rows else 0


def get_list_of_pomodoros(days: int, limit: int) -> list[list[str]]:
    interval = f"-{9999 if days == -1 else days} days"
    query = """
        SELECT DATETIME(created_at, 'localtime') AS created_at, minutes, tag
        FROM pomodoros
        WHERE created_at >= DATETIME('now', ?)
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
    if not rows:
        return [["There are no pomodoros yet"]]

    return [
        [str(row["created_at"]), str(row["minutes"]), str(row["tag"] or "-")]
        for row in rows
    ]


def get_list_of_tags(days: int) -> list[str]:
    interval = f"-{9999 if days == -1 else days} days"
    query = """
            SELECT DISTINCT tag
            FROM pomodoros
            WHERE created_at >= DATETIME('now', ?)
        """
    rows = execute_query(query, (interval,))
    if not rows:
        return ["There are not tags yet"]
    return [str(row[0] or "-") for row in rows]


def get_average_of_days(days: int) -> float:
    interval = f"-{days} days"
    average_of_tags = -1
    query = """
            SELECT COUNT(minutes) * 1.0/ ?
            FROM pomodoros
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
        average_of_tags = round(average_output[0][0], 1)
    return average_of_tags
