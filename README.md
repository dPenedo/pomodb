# pomodb

A Pomodoro timer for the terminal that stores every session in SQLite.

I spend most of the day in a terminal, so I wanted the timer there too. Most Pomodoro apps forget a session as soon as it ends; pomodb keeps each one with an optional tag, so at the end of the week I can see how many pomodoros actually went to each project.

It only uses the Python standard library.

## Requirements

- Python 3.11 or newer.
- `ffplay` (part of FFmpeg) to play the gong at the start and end of each period.
- `notify-send` for desktop notifications (optional, Linux only).

## Installation

```sh
git clone https://github.com/dPenedo/pomodb.git
cd pomodb
pipx install .
```

This installs the `pomodb` command. `uv tool install .` works too. To run it without installing, use `python -m pomodoro` from the repository root.

## Usage

```sh
pomodb                          # Asks for a tag and starts 4 pomodoros
pomodb start                    # Starts 4 pomodoros without a tag
pomodb start -n 2 -t writing    # 2 pomodoros tagged "writing"
pomodb stats                    # Totals, tags and the last 20 pomodoros
pomodb create-config            # Writes the default config file
pomodb help
```

Before starting, it prints the time at which the whole session will end. `Ctrl+C` stops the session; pomodoros that were already finished stay saved.

## Configuration

pomodb works without a config file. To change the defaults, create one:

```sh
pomodb create-config
```

It is written to `~/.config/pomodb/config.toml` (or `$XDG_CONFIG_HOME/pomodb/` if that variable is set):

```toml
[pomodoro]
minutes = 25
break_minutes = 5

[notifications]
enabled = true
```

Any key you leave out falls back to its default value.

## Stored data

Each finished pomodoro is saved in `~/.local/share/pomodb/pomodoros.db` (or `$XDG_DATA_HOME/pomodb/`), in a table called `pomodoros`:

- `id`: unique identifier.
- `created_at`: when the pomodoro finished, in UTC.
- `minutes`: duration of the pomodoro.
- `message`: always `🍅 Pomodoro` for now.
- `tag`: the session tag, or `NULL` if none was given.

Since it is a plain SQLite file, you can query it directly for anything `pomodb stats` does not show:

```sh
sqlite3 ~/.local/share/pomodb/pomodoros.db \
  "SELECT tag, COUNT(*) FROM pomodoros GROUP BY tag ORDER BY 2 DESC"
```

## License

[MIT](LICENSE)
