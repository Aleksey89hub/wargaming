import os
import re
from typing import List


def clean_text_from_brackets(text: str) -> str:
    """Removes  brackets containing numbers (e.g., [2], [3]) from the given string."""
    return re.sub(r'\[\d+]', '', text).strip()


def list_comprehension_digits(text: str) -> str:
    """Extracts only the digits from the given string using list comprehension."""
    return ''.join([char for char in text if char.isdigit()])


def get_variable(name: str) -> str:
    """
    Get the value of the required environment variable.
    Raises: ValueError: If the environment variable is not set.
    """
    value = os.environ.get(name)
    if value is None:
        raise ValueError(f"Environment variable '{name}' is required but not set.")
    return value


def print_grid(grid: List[List[str]]) -> None:
    """
    Prints the grid in a human-readable format.
    """
    for row in grid:
        print(' '.join(row))
