import json
import os
from dotenv import load_dotenv
import requests


load_dotenv()
API_KEY = os.getenv("API_KEY")
HOST = "real-time-events-search.p.rapidapi.com"


def get_json(query, date):
    """
    Fetches event data for a given location and date, and saves it to 'response.json'.
    """
    api_url = f"https://{HOST}/search-events?query={query}&is_virtual=false&date={date}"
    headers = {
        "x-rapidapi-key": API_KEY,
    }

    # simple connection test
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            title_data_json = response.json()
            with open("response.json", "w") as fileobj:
                json.dump(title_data_json, fileobj)
        else:
            print(f"Error occurred: {response.status_code}")

    except requests.exceptions.ConnectionError as e:
        print("ConnectionError: ", e)