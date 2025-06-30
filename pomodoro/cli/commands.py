import os


def show_stats():
    # TODO: query()
    log_file = "./log.txt"
    if not os.path.exists(log_file):
        print("There are no stats yet")
        return
    with open(log_file, "r") as f:
        print("\n📊 Pomodoro statistics")
        print("-" * 40)
        print(f.read())
        print("-" * 40)


def show_help():
    help_text = """
🍅 Pomodoro CLI - Manual de uso

Comandos disponibles:
  start     Inicia una nueva sesión de pomodoros
  stats     Muestra estadísticas de sesiones anteriores
  help      Muestra este mensaje de ayuda

Ejemplos:
  py pomodoro.py start -n 4 -t "proyectoX"
  py pomodoro.py stats
  py pomodoro.py help
"""
    print(help_text)
