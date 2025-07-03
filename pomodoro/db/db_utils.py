import sqlite3
from typing import Any, Tuple
from pomodoro.db.models import get_db_connection


def execute_query(query: str, params: Tuple[Any, ...] = ()):
    try:
        with get_db_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
    except Exception as e:
        print(f"Error executing query {e}")
        return None


def execute_non_query(query: str, params: Tuple[Any, ...] = ()):
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return True

    except Exception as e:
        print(f"Error executing non-query {e}")
        return False
