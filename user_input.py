# import dateparser
from geopy.geocoders import Nominatim
import re


def process_user_input(user_input):
    input_to_parse = user_input.lower().strip()
    # any, today, tomorrow, week, weekend, next_week, month, next_month
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


    # day_to_validate = match.group(2).strip()
    print(city_to_validate, time)

    # geolocator = Nominatim(user_agent="city_validator")
    # location = geolocator.geocode(city_to_validate, exactly_one=True)

    # parsed_date = dateparser.parse(day_to_validate, settings={"PREFER_DATES_FROM": "future"}, languages=["en"])

    # if location and location.latitude and location.longitude:
    #     # print(f"City '{city_to_validate}' is valid.")
    #     location = city_to_validate
    #
    # else:
    #     return f"City '{city_to_validate}' is invalid."

    # if parsed_date:
    #     date = parsed_date.strftime("%Y-%m-%d")
    #
    # else:
    #     return f"Invalid date."

    return city_to_validate, time



# user_input = input("Enter city and day or date: ")
# result = process_user_input(user_input)
# print(result)





