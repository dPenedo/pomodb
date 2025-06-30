from pomodoro.db.models import get_db_connection
from pomodoro.utils.constants import POMODORO_TABLE


def log_a_pomodoro(minutes: int, message: str, tag: str | None):
    connection = get_db_connection()

    if connection:
        try:
            cursor = connection.cursor()
            _ = cursor.execute(
                f"""
            INSERT INTO {POMODORO_TABLE} ( minutes, message, tag)
            VALUES (?, ?, ?)
            """,
                (minutes, message, tag or ""),
            )
            _ = connection.commit()
            print("Pomodo registered")
        except Exception as e:
            print(f"Error registering de pomodoro {e}")
        finally:
            connection.close()
    else:
        print("Failed to establish connection")
