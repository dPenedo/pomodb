from pomodoro.cli.show_help import show_help
from pomodoro.cli.parser import parse_args
from pomodoro.countdown import countdown
from pomodoro.config import create_config, load_config
from pomodoro.utils.format import cyan
from pomodoro.utils.stats import get_stats
from pomodoro.utils.total_time import get_total_time


def main():
    args = parse_args()

    command = getattr(args, "command", None)
    num_pomodoros = getattr(args, "number_of_pomodoros", 4)
    pomodoro_tags = getattr(args, "tags_of_pomodoros", None)

    if command == "start" or command is None:
        if command is None:
            tag = input("Tag (enter to skip): ").strip() or None
            pomodoro_tags = tag
        try:
            config = load_config()
            print(get_total_time(num_pomodoros, config.minutes, config.break_minutes))
            for i in range(0, num_pomodoros):
                pomodoro_position = f"{i + 1} of {num_pomodoros}"
                print(f"You are on pomodoro {cyan(pomodoro_position)}")
                _ = countdown(
                    minutes=config.minutes,
                    work=True,
                    notifications_enabled=config.notifications_enabled,
                    tag=pomodoro_tags,
                )
                _ = countdown(
                    minutes=config.break_minutes,
                    work=False,
                    notifications_enabled=config.notifications_enabled,
                    tag=pomodoro_tags,
                )
        except KeyboardInterrupt:
            print("\n👋 Session is over.")
    elif command == "help":
        show_help()
    elif command == "stats":
        print(get_stats())
    elif command == "create-config":
        print(create_config())
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
