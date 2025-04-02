import os
from dotenv import load_dotenv
import json


load_dotenv()
USER_NUMBER = os.getenv('PHONE_NUMBER')


def get_user_data(location, event_type, date):
    """follows"""

    while True:
        try:
            with open("user_data.json", "r") as fileobject:
                records = json.load(fileobject)
                break

        except FileNotFoundError:
            with open("user_data.json", 'w') as fileobject:
                fileobject.write("[]")

    if records:
        new_id = max(record["query_id"] for record in records) + 1
    else:
        new_id = 1

    new_record = {
        "user_number": USER_NUMBER,
        "query_id": new_id,
        "location": location,
        "time": date,
        "event type": event_type
    }

    records.append(new_record)

    file_path = "user_data.json"
    with open(file_path, "w", encoding="utf-8") as fileobj:
        json.dump(records, fileobj, indent=4)


