import json

def extract_event_info(file_path: object) -> object:
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
    for event in data.get("data", [])[:3]:  # Slice to get only the first 3 events
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
        message = f'''*{event["name"]}*\n\n{event["date_human_readable"]} \n\n*_more on this event:_* {event["link"]}\n\n{event["description"]}'''
        event_messages.append(message)

    return event_messages


def main():
    """
    Main function that orchestrates the flow of the program.
    It loads event data from a file, extracts event information, and formats the responses.
    """
    # Specify the path to your JSON file
    file_path = "response.json"  # Replace with the path to your JSON file

    # Extract event information from the JSON file
    events = extract_event_info(file_path)

    # If events are extracted, format them into messages
    if events:
        messages = twilio_response(events)
        # Print or use the messages as needed
        for message in messages:
            print(message)
    else:
        print("No events to process.")


# Ensure the main function is called when the script is executed
if __name__ == "__main__":
    main()
