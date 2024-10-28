import requests
import argparse
import importlib
import os
from solver import AdventSolver
from typing import NoReturn
from dotenv import load_dotenv

load_dotenv()


def get_solver_class(year: int, day: int) -> type[AdventSolver]:
    """Import and return the solver class for the given day."""
    try:
        module = importlib.import_module(f"year_{year}.day_{day}")

        # Look for a class that implements AdventSolver
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if (
                isinstance(attr, type)
                and issubclass(attr, AdventSolver)
                and attr != AdventSolver
            ):
                return attr

        raise ImportError(f"No AdventSolver implementation found for day {day}")

    except ImportError as e:
        raise ImportError(f"Failed to load solver for day {day}: {e}")


def format_input_file_location(year: int, day: int) -> str:
    return f"input/year_{year}/day_{day}.txt"


def pull_days_input(year: int, day: int) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    print(f"Requesting data from {url}")
    r = requests.get(url, headers={"Cookie": os.getenv("COOKIE")})
    file_path = format_input_file_location(year, day)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Now write the file
    with open(file_path, "w+") as f:
        f.write(r.text)

    print(
        "Succesfully pulled data from website, and saved to local file for future use"
    )
    return r.text


def load_days_input(year: int, day: int) -> list[str]:
    try:
        print(f"Trying to open input file at {format_input_file_location(year, day)}")
        input_data = open(format_input_file_location(year, day))
        print("Succesfully pulled data from file")
        return input_data.read().split("\n")
    except:
        print("Did not find file, pulling website now")
        return pull_days_input(year, day).split("\n")


def parse_args() -> argparse.Namespace:
    """Set up and parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Process data for a specific day and year"
    )

    parser.add_argument(
        "--day",
        type=int,
        required=True,
        help="Which day to process (1-31)",
        choices=range(1, 32),  # Validates day range
        metavar="DAY",  # Makes help message clearer
    )

    parser.add_argument(
        "--year",
        type=int,
        default=2015,  # Makes year optional with default
        help="Which year to process (default: %(default)s)",
        choices=range(2015, 2024),
    )

    return parser.parse_args()


def run_day() -> None:
    print("Starting")
    args = parse_args()
    print(f"Parsed args were year={args.year}, day={args.day}")
    solver_class = get_solver_class(args.year, args.day)
    solver = solver_class()
    data = load_days_input(args.year, args.day)
    print(solver.part_1(input_data=data))
    print(solver.part_2(input_data=data))


if __name__ == "__main__":
    run_day()
