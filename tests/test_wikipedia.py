from typing import Callable
import pytest


class TestWikipediaProgramingTable:
    """Tests the data in the Wikipedia table of programming languages used in most popular websites."""
    TEST_DATA = [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9]

    @pytest.mark.parametrize("min_popularity", TEST_DATA)
    def test_programming_languages_popularity(self,
                                              fetch_data: Callable,
                                              min_popularity: int, ):
        """Tests that the popularity of each programming language in the table is greater
         than or equal to the given minimum popularity.
        """
        table_data = fetch_data()
        errors = []

        for entry in table_data:
            if int(entry['popularity']) < min_popularity:
                error_message = (
                    f"{entry['site']} (Frontend: {entry['frontend']} | Backend: {entry['backend']}) "
                    f"has {entry['popularity']} unique visitors per month. "
                    f"(Expected more than {min_popularity})"
                )
                errors.append(error_message)

        assert not errors, "\n".join(errors)
