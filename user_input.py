import re


def process_location_time(user_input):
    """
    Function gets user input and returns location and time.
    """
    input_to_parse = user_input.lower().strip()

    pattern = r"^(.*?)\s+((?:next\s+(?:week|month))|any|today|tomorrow|weekend|week|month)$"
    match = re.match(pattern, input_to_parse, re.UNICODE)

    if not match:
        return "Invalid input."

    city = match.group(1).strip()

    time = match.group(2).strip()
    if time == "next week":
        time = "next_week"

    elif time == "next month":
        time = "next_month"

    return city, time


def process_event_type(user_input):
    pass



