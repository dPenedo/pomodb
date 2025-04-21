from datetime import datetime, timedelta
from pomodoro.utils.format import prPurple

def get_total_time(number_of_pomodoros, work_minutes, rest_minutes):
    now = datetime.now()
    total_minutes_to_add = (work_minutes * number_of_pomodoros) + (rest_minutes * number_of_pomodoros)
    end_time = now + timedelta(minutes=total_minutes_to_add)

    from_to_text = f"from {prPurple(now.hour)}:{prPurple(now.minute)} to {prPurple(end_time.hour)}:{prPurple(end_time.minute)}"

    return f"Your pomodoros go {from_to_text} "

