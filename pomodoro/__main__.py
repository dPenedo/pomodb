from pomodoro.cli.commands import show_help
from pomodoro.cli.parser import parse_args
from pomodoro.countdown import countdown
from pomodoro.utils.format import prCyan
from pomodoro.utils.constants import WORK, REST
from pomodoro.utils.stats import get_stats
from pomodoro.utils.total_time import get_total_time


def main():
    args = parse_args()

    command = getattr(args, "command", None)
    num_pomodoros = getattr(args, "number_of_pomodoros", 4)
    pomodoro_tags = getattr(args, "tags_of_pomodoros", None)

    if command == "start":
        print(get_total_time(num_pomodoros, WORK["minutes"], REST["minutes"]))
        try:
            for i in range(0, num_pomodoros):
                pomodoro_position = f"{i+1} of {num_pomodoros}"
                print(f"You are on pomodoro {prCyan(pomodoro_position)}")
                _ = countdown(
                    WORK["minutes"],
                    WORK["text"],
                    WORK["action"],
                    pomodoro_tags,
                )
                _ = countdown(REST["minutes"], REST["text"], REST["action"])
        except KeyboardInterrupt:
            print("\n👋 Session is over.")
    elif command == "help":
        show_help()
    elif command == "stats":
        print(get_stats())
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
