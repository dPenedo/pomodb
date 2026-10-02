from dataclasses import dataclass, replace
import tomllib

from pomodoro.paths import get_config_dir, get_config_file


DEFAULT_CONFIG_TOML = """\
[pomodoro]
minutes = 25
break_minutes = 5

[notifications]
enabled = true
"""

# TODO: implement hooks
"""
[hooks]
# focus_start = ["dunstctl set-paused true"] # Pause dunst

# focus_start = ["makoctl mode -a do-not-disturb"]   # DND on mako
# focus_start = ["gsettings set org.gnome.desktop.notifications show-banners false"]  # DND on GNOME
# focus_start = ["pkill -x slack"] # Kill Slack
# focus_end = ["echo \"$(date -Iseconds) $POMODB_TAG\" >> ./focus.log"] # Log the date to a file
# break_start = ["dunstctl set-paused false"] # Resume dunst
# session_end = ["dunstctl set-paused false"] # Resume dunst
"""


@dataclass
class Config:
    minutes: int
    break_minutes: int
    notifications_enabled: bool
    # TODO: create hooks logic
    # hooks: dict[str, list[str]] | None


def create_config() -> str:
    if get_config_file().exists():
        return f"There is already a config in {str(get_config_dir())}"
    path = get_config_dir()
    config_file = get_config_file()
    _ = path.mkdir(parents=True, exist_ok=True)
    _ = config_file.write_text(DEFAULT_CONFIG_TOML, encoding="utf-8")
    return f"Config created in {str(get_config_dir())}"


def load_config() -> Config:
    config = Config(minutes=25, break_minutes=5, notifications_enabled=True)
    # TODO: config = Config(minutes=25, break_minutes=5, notifications_enabled=True, hooks=None)

    if get_config_file().exists():
        try:
            with open(get_config_file(), "rb") as f:
                data = tomllib.load(f)
                updated_config = replace(
                    config,
                    minutes=data.get("pomodoro", {}).get("minutes", config.minutes),
                    break_minutes=data.get("pomodoro", {}).get(
                        "break_minutes", config.break_minutes
                    ),
                    notifications_enabled=data.get("notifications", {}).get(
                        "enabled", config.notifications_enabled
                    ),
                )
            return updated_config

        except Exception as e:
            print(f"Error reading the config: \n{e}")

    return config
