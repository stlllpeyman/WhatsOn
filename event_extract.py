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
            f"Hark thee, thou art a clodpole, a lack-brain! Forsooth, no merriments nor happenings are to be found within this {location}.",
            f"Fie on thee, thou art as empty-witted as a gull! Verily, no pageants nor pastimes do grace {location}'s streets.",
            f"Avaunt, thou art a scurvy knave, a most base footlicker! Alas, no tidings of revelry or show reach this place of {location}.",
            f"By the heavens, thou art a dullard, a thrice-sodden fool! In truth, no jests nor entertainments do stir in {location}.",
            f"Go to, thou art a witless worm, a very drone! Alack, no feasts nor festivals are discovered within the bounds of {location}."
            f"Thou sodden-witted lord! Thou hast no more brain than I have in mine elbows. Alas, it is so that in {location}, no stirring dances nor melodious concerts do grace the hour"]

        messages = [random.choice(insults)]
        print("No events to process.")
        return messages



