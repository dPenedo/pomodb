import os

_SOUNDS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sounds')


def play(filename: str):
    path = os.path.join(_SOUNDS_DIR, filename)
    os.system(f'ffplay -nodisp -autoexit -loglevel quiet "{path}" &')
