import sys
import time

from exceptions import InvalidInputError


class Color:

    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"


BANNER = r"""
   _____                      _      _____      _
  / ____|                    | |    / ____|    | |
 | (___  _ __ ___   __ _ _ __| |_  | |     __ _| | ___
  \___ \| '_ ` _ \ / _` | '__| __| | |    / _` | |/ __|
  ____) | | | | | | (_| | |  | |_  | |___| (_| | | (__
 |_____/|_| |_| |_|\__,_|_|   \__| \_____\__,_|_|\___|
"""


def print_banner() -> None:
    print(f"{Color.CYAN}{Color.BOLD}{BANNER}{Color.RESET}")
    print(f"{Color.YELLOW}      Smart Calculator CLI — Python Portfolio Project{Color.RESET}\n")


def loading_animation(message: str = "Menghitung", duration: float = 0.6) -> None:
    steps = 3
    delay = duration / steps
    sys.stdout.write(f"{Color.MAGENTA}{message}{Color.RESET}")
    sys.stdout.flush()
    for _ in range(steps):
        time.sleep(delay)
        sys.stdout.write(f"{Color.MAGENTA}.{Color.RESET}")
        sys.stdout.flush()
    print()


def parse_number(raw: str) -> float:
    try:
        return float(raw.strip().replace(",", "."))
    except (ValueError, AttributeError) as exc:
        raise InvalidInputError(f"'{raw}' bukan angka yang valid.") from exc


def read_number(prompt: str) -> float:
    while True:
        try:
            return parse_number(input(f"{Color.BLUE}{prompt}{Color.RESET}"))
        except InvalidInputError as error:
            print(f"{Color.RED}[!] {error}{Color.RESET}")


def format_number(value: float) -> str:
    if value == int(value):
        return str(int(value))
    return f"{value:g}"
