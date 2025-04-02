import re
import requests
from store_events import API_KEY


def validate_city(city):
    """
    Function uses City Search API to validate the city.
    """
    city = city.lower().capitalize()

    url = f"https://city-search2.p.rapidapi.com/city/autocomplete?input={city}"  # Adjust based on API
    headers = {
        "X-RapidAPI-Key": API_KEY
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    if data and len(data['data']) > 0:
        for item in data["data"]:
            if item['name'] == city:
                # valid city
                return city
    else:
        # invalid city
        return None

    return None

def process_location_time(user_input):
    """
    Function gets user input and returns location and time.
    """
    input_to_parse = user_input.lower().strip()
    pattern = r"^(.*?)\s+((?:next\s+(?:week|month))|any|today|tomorrow|weekend|week|month)$"
    match = re.match(pattern, input_to_parse, re.UNICODE)

    if not match:
        return "Invalid input."

    city_to_validate = match.group(1).strip()
    time = match.group(2).strip()

    if time == "next week":
        time = "next_week"

    elif time == "next month":
        time = "next_month"

    validated_city = validate_city(city_to_validate)

    if not validated_city:
        return None, time

    return validated_city, time
