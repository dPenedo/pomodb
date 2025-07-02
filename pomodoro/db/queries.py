from typing import List
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
    if time == -1:
        time = 99999

    if connection:
        try:
            cursor = connection.cursor()
            _ = cursor.execute(
                f"""
                SELECT SUM(minutes)
                FROM {POMODORO_TABLE}
                WHERE created_at >= (SELECT DATETIME('now', '-{time} days'))
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


def get_list_of_pomodoros(time: int) -> List[str]:
    list_of_pomodoros = ["There are no pomodoros yet"]
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            _ = cursor.execute(
                f"""
                SELECT * FROM {POMODORO_TABLE}
                WHERE created_at >= (SELECT DATETIME('now', '-{time} days'))
                """
            )
            list_of_pomodoros_tuples = cursor.fetchall()
            print("list_of_pomodoros_tuples => ", list_of_pomodoros_tuples)
            list_of_pomodoros.clear()
            # WARN: no va
            # for e in list_of_pomodoros_tuples:
            #     list_of_pomodoros.append(str(e))
            print("list_of_pomodoros => ", list_of_pomodoros)
        except Exception as e:
            print(f"Error accessing to the list of pomodoros: {e}")

    return list_of_pomodoros


def get_list_of_tags(time: int) -> List[str]:
    connection = get_db_connection()
    list_of_tags = ["There are not tags yet"]
    if connection:
        try:
            cursor = connection.cursor()
            _ = cursor.execute(
                f"""
                SELECT DISTINCT tag
                FROM {POMODORO_TABLE}
                WHERE created_at >= (SELECT DATETIME('now', '-{time} days'))
                """
            )
            list_of_tag_tuples = cursor.fetchall()
            list_of_tags.clear()
            for e in list_of_tag_tuples:
                list_of_tags.append(str(e[0]))
            cursor.close()
        except Exception as e:
            print(f"Error accessing to the list of tags {e}")
    else:
        print("Failed to access to list of tags")
    return list_of_tags
