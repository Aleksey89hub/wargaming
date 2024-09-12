from typing import Callable
import pytest
from src.wikipedia_parser import fetch_table_data


@pytest.fixture(scope='session')
def fetch_data() -> Callable:
    """
    Fixture to fetch and cache table data from a Wikipedia page about
    programming languages used in popular websites.
    """
    data_cache = None

    def get_data() -> list[dict]:
        nonlocal data_cache
        if data_cache is None:
            data_cache = fetch_table_data()
        return data_cache

    return get_data
