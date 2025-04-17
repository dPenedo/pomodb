from pomodoro.cli.commands import show_help, show_stats
from pomodoro.cli.parser import parse_args
from pomodoro.countdown import countdown
from pomodoro.utils.format import prCyan
from pomodoro.utils.constants import WORK, REST


def main():
    args = parse_args()

    if args.command == "start":
        try:
            for i in range(0, args.number_of_pomodoros):
                position_of_pomodoros = f"{i+1} of {args.number_of_pomodoros}"
                print(f"You are on pomodoro {prCyan(position_of_pomodoros)}")
                countdown(
                    WORK["minutes"],
                    WORK["text"],
                    WORK["action"],
                    args.tags_of_pomodoros,
                )
                countdown(REST["minutes"], REST["text"], REST["action"])
        except KeyboardInterrupt:
            print("\n👋 Session is over.")
    elif args.command == "help":
        show_help()
    elif args.command == "stats":
        show_stats()
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
