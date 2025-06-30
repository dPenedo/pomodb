from datetime import datetime, timedelta
from pomodoro.utils.format import prPurple


def get_total_time(number_of_pomodoros: int, work_minutes: int, rest_minutes: int):
    now = datetime.now()
    total_minutes_to_add = (work_minutes * number_of_pomodoros) + (
        rest_minutes * number_of_pomodoros
    )
    end_time = now + timedelta(minutes=total_minutes_to_add)

    from_to_text = f"from {prPurple(str(now.hour))}:{prPurple(str(now.minute))} to {prPurple(str(end_time.hour))}:{prPurple(str(end_time.minute))}"

    return f"Your pomodoros go {from_to_text} "
