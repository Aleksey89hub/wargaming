import requests
from bs4 import BeautifulSoup
from helper.tools import clean_text_from_brackets, list_comprehension_digits, get_variable


def fetch_table_data() -> list[dict]:
    """
        Fetches data from the Wikipedia page on programming languages used
        in the most popular websites and parses the table of information.
    """
    response = requests.get(get_variable("API_WIKIPEDIA_URL"))
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    data = []

    for row in table.find_all('tr')[1:]:
        columns = row.find_all('td')
        if len(columns) >= 4:
            site_name = clean_text_from_brackets(columns[0].get_text(strip=True))
            popularity = list_comprehension_digits(columns[1].get_text(strip=True).replace(',', ''))
            frontend = clean_text_from_brackets(columns[2].get_text(strip=True))
            backend = clean_text_from_brackets(columns[3].get_text(strip=True))

            data.append({
                'site': site_name,
                'frontend': frontend,
                'backend': backend,
                'popularity': popularity
            })

    return data
