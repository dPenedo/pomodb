from sqlite3 import Connection
import sqlite3

from pomodoro.paths import get_data_file


def init_db(conn: Connection):
    """Initalize the Database"""
    _ = conn.execute(
        """
        CREATE TABLE IF NOT EXISTS pomodoros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                minutes INTEGER NOT NULL,
                message TEXT NOT NULL,
                tag TEXT )
    """
    )
    _ = conn.commit()


def get_db_connection() -> Connection:
    """Ensure DB exists and return connection"""
    conn = sqlite3.connect(get_data_file())
    try:
        init_db(conn)
    except sqlite3.Error:
        conn.close()
        raise
    return conn
