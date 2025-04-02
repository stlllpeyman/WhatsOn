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
    # our Twilio messaging service (our workspace where conversations happen)
    # <service> is like a folder that hold all conversations
    service = tw.init_twilio_client()
    
    address = f"whatsapp:{os.getenv('PHONE_NUMBER')}"
    ms_address = f"whatsapp:{os.getenv('MS_WHATSAPP_NUMBER')}"
    # file_path = "response.json"
    # events = extract_event_info(file_path)
    #
    # my_conversation = get_my_conversation(service, address) or create_my_conversation(service, address, ms_address)

    # checks if convo exists <or> (if not existing) creates a new one convo
    my_conversation = tw.get_my_conversation(service, address) or tw.create_my_conversation(service, address, ms_address)

    while True:
        user_message = tw.wait_for_user_message(my_conversation, address)
        api_query = process_location_time(user_message)

        try:
            location, date = api_query
            get_json(location, date)
            tw.send_message(my_conversation, "Certainly, this is WhatsOn:")
            responses = event.get_formatted_events(location)

            ##### user types: location + time
            ##### bot response with cool: pick event type from list
            ##### user picks, we then query the API for the first time

            # filter the responses
            for response in responses:
                tw.send_message(my_conversation, response)

        except ValueError:
            tw.send_message(my_conversation, "Please keep it short :) example: 'berlin tomorrow'")


if __name__ == "__main__":
    main()
