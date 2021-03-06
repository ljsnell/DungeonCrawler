import os


def clear_display():
    os.system('cls' if os.name == 'nt' else 'clear')
