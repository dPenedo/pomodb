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


def get_sum_of_minutes(time: int) -> int:
    connection = get_db_connection()
    number_of_minutes = -1

    if connection:
        try:
            cursor = connection.cursor()
            _ = cursor.execute(
                f"""
                SELECT SUM(minutes) FROM {POMODORO_TABLE}
                """
            )
            sum_of_minutes = cursor.fetchall()
            number_of_minutes = sum_of_minutes[0][0]
            cursor.close()
        except Exception as e:
            print(f"Error accessing to sum of minutes {e}")

    else:
        print("Failed to access to sum of minutes")

    return number_of_minutes
