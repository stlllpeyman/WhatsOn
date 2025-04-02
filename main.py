import os
import twilio_helpers as tw
from user_input import process_location_time
import event_extract as event
from store_events import get_json


def main():
    """
    Main function initializes Twilio and retrieves messaging service,
    formats the phone numbers for Twilio (that is why use of f-string),
    checks if convo exists, if not creates one,keeps waiting for messages and responding
    """
    # Twilio messaging service (our workspace where conversations happen)
    service = tw.init_twilio_client()
    
    address = f"whatsapp:{os.getenv('PHONE_NUMBER')}"
    ms_address = f"whatsapp:{os.getenv('MS_WHATSAPP_NUMBER')}"

    my_conversation = tw.get_my_conversation(service, address) or tw.create_my_conversation(service, address, ms_address)

    while True:
        user_message = tw.wait_for_user_message(my_conversation, address)
        api_query = process_location_time(user_message)

        try:
            location, date = api_query
            tw.send_message(my_conversation, "Cool! What type of event are you looking for? football, concert, movie?")
            user_event_type = tw.wait_for_user_message(my_conversation, address)
            event_type = user_event_type
            query = event_type + " " + location
            # print(query)
            tw.send_message(my_conversation, "Certainly, this is WhatsOn:")
            get_json(query, date)

            responses = event.get_formatted_events(location)
            for response in responses:
                tw.send_message(my_conversation, response)

        except ValueError:
            tw.send_message(my_conversation, "Please keep it short :) example: 'berlin tomorrow'")


if __name__ == "__main__":
    main()
