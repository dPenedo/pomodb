from contextlib import closing
import sqlite3
from typing import Any
from pomodoro.db.models import get_db_connection


def execute_query(query: str, params: tuple[Any, ...] = ()) -> list[sqlite3.Row] | None:
    try:
        with closing(get_db_connection()) as conn:
            conn.row_factory = sqlite3.Row
            return conn.execute(query, params).fetchall()
    except Exception as e:
        print(f"Error executing query {e}")
        return None


def execute_non_query(query: str, params: tuple[Any, ...] = ()) -> bool:
    try:
        with closing(get_db_connection()) as conn, conn:
            conn.execute(query, params)
            return True

    except Exception as e:
        print(f"Error executing non-query {e}")
        return False
