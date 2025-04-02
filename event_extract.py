import json
import random
import textwrap


def extract_event_info(file_path: str) -> list[dict]:
    """
    Extracts the first 3 events (or fewer) from the JSON file at the given path.
    Returns a list of dictionaries containing event details.
    """
    event_list = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("The file was not found.")
        return []

    except json.JSONDecodeError:
        print("Error decoding the JSON file.")
        return []

    # Extract the first 3 events
    for event in data.get("data", [])[:3]:
        event_data = {
            "name": event.get("name", "Name is not available"),
            "description": event.get("description", "Description is not available"),
            "date_human_readable": event.get("date_human_readable", "Date is not available"),
            "link": event.get("link", "Link is not available"),
        }
        event_list.append(event_data)

    return event_list


def twilio_response(events):
    """
    Accepts a list of event dictionaries and returns a list of formatted messages for each event.
    """
    event_messages = []

    # Loop through each event and format the message
    for event in events:
        message = f"""
        *{event["name"]}*
        
        {event["date_human_readable"]}
        
        *_more on this event:_* {event["link"]}

        {event["description"]}"""

        # textwrap.dedent cleans up leading spaces from multiline strings
        event_messages.append(textwrap.dedent(message))

    return event_messages


def get_formatted_events(location):
    """
    Retrieves event data from a JSON file, extracts relevant information,
    and formats event details into messages suitable for Twilio responses.
    If events are found, it returns a list of formatted event messages.
    If no events are available, it returns a humorous response.
    Parameter "location": The location for which events are being searched.
    """
    # Specify the path to your JSON file
    file_path = "response.json"  # Replace with the path to your JSON file

    # Extract event information from the JSON file
    events = extract_event_info(file_path)

    # If events are extracted, format them into messages
    if events:
        messages = twilio_response(events)
        return messages

    else:
        insults = [
            f"Ah, {location}! A place where even time itself seems to have packed up and left.",
            f"By Jove, {location} is as lively as a crypt at midnight!",
            f"{location}, my dear fellow, has all the excitement of a damp cravat.",
            f"Holmes, I do believe {location} is where fun goes to perish.",
            f"Nothing in {location}, old boy—unless one counts the thrilling sound of paint drying.",
            f"Ah, {location}, a veritable festival of stillness and despair!",
            f"Unless one considers watching the clouds an event, {location} is tragically bereft of activity.",
            f"My dear chap, {location} makes a library on a Sunday seem positively riotous!",
            f"As empty as a detective’s pipe before breakfast—{location} offers naught but solitude!",
            f"{location}, where even the tumbleweeds have given up and gone elsewhere."
        ]

        insult = random.choice(insults)
        print("No events to process.")
        return insult



