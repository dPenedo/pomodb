import os
from pathlib import Path


APP_NAME = "pomodb"


def get_config_dir() -> Path:
    base = os.environ.get("XDG_CONFIG_HOME") or Path.home() / ".config"
    return Path(base) / APP_NAME


def get_config_file() -> Path:
    config_file = get_config_dir() / "config.toml"
    return config_file


def get_data_dir() -> Path:
    base = os.environ.get("XDG_DATA_HOME") or Path.home() / ".local" / "share"
    return Path(base) / APP_NAME


def get_data_file() -> Path:
    data_dir = get_data_dir()
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / "pomodoros.db"
