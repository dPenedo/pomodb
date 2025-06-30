from sqlite3 import Connection
import sqlite3

from pomodoro.utils.constants import DB_FILENAME, POMODORO_TABLE


def init_db(conn: Connection):
    """Initalize the Database"""
    _ = conn.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {POMODORO_TABLE} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                minutes INTEGER NOT NULL,
                message TEXT NOT NULL,
                tag TEXT NOT NULL )
    """
    )
    _ = conn.commit()


def get_db_connection() -> Connection | None:
    """Ensure DB exists and return connection"""
    try:
        conn = sqlite3.connect(DB_FILENAME)
        init_db(conn)
        return conn

    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None
