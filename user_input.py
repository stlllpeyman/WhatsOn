import dateparser
from geopy.geocoders import Nominatim
import re


def process_user_input(text):
    input_to_parse = user_input.lower().strip()
    pattern = r"([a-zA-Z\s]+)\s+(next|tomorrow|\w+\s\d{1,2}|[a-zA-Z]+day)$"
    match = re.match(pattern, input_to_parse)

    if not match:
        return "Invalid input."

    city_to_validate = match.group(1).strip()
    day_to_validate = match.group(2).strip()

    geolocator = Nominatim(user_agent="city_validator")
    location = geolocator.geocode(city_to_validate)
    parsed_date = dateparser.parse(day_to_validate, settings={"PREFER_DATES_FROM": "future"}, languages=["en"])

    if location:
        print(f"City '{city_to_validate}' is valid.")

    else:
        return f"City '{city_to_validate}' is invalid."

    if parsed_date:
        return parsed_date.strftime("%Y-%m-%d")

    else:
        return f"Invalid date."



user_input = input("Enter city and day or date: ")
result = process_user_input(user_input)
print(result)





