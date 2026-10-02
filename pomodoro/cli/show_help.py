def show_help():
    help_text = """
🍅 Pomodoro CLI - Usage

Commands:
  start           Start a pomodoro session
  stats           Show statistics from previous sessions
  help            Show this help message
  create-config   Create a config file with the default values

Options for start:
  -n, --number-of-pomodoros N   Number of pomodoros (default: 4)
  -t, --tags-of-pomodoros TAG   Tag of the session

Examples:
  python -m pomodoro start -n 4 -t "Refactor the whole FastApi backend of the client"
  python -m pomodoro start -t "Fix cart on WooCommerce"
  python -m pomodoro stats
  python -m pomodoro help
  python -m pomodoro create-config
"""
    print(help_text)
