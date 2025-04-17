import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="🍅 Pomodoro CLI timer - Get focus!")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    start_parser = subparsers.add_parser("start", help="Start a new pomodoro session")
    start_parser.add_argument(
        "-n",
        "--number-of-pomodoros",
        type=int,
        default=4,
        help="Number of pomodoros (default: 4)",
    )
    start_parser.add_argument(
        "-t",
        "--tags-of-pomodoros",
        type=str,
        help="Tags of pomodoros",
    )

    subparsers.add_parser("stats", help="View previous stats")
    subparsers.add_parser("help", help="Get help about this pomodoro")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()
