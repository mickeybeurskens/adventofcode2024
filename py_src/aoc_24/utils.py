from pathlib import Path

INPUTS_DIR = Path(__file__).parent.parent.parent / "inputs"


def get_day_input(day: int) -> str:
    return INPUTS_DIR.joinpath(f"day{day}.txt").read_text()
