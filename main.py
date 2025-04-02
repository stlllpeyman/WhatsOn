import os
import twilio_helpers as tw
from user_input import process_location_time
import event_extract as event
from store_user_data import get_user_data
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

            if location is None:
                tw.send_message(my_conversation, "Good Lord! I have never heard of this locale ...")

            else:
                tw.send_message(my_conversation, """
                My dear fellow, sport, concert, or something refined?\n(Enter something like sports, concert, movie or any.)
                """)
                user_event_type = tw.wait_for_user_message(my_conversation, address)
                event_type = user_event_type
                query = event_type + " " + location

                get_user_data(location, event_type, date)

                get_json(query, date)

                responses = event.get_formatted_events(location)
                if type(responses) == list:
                    tw.send_message(my_conversation,
                                    f"Capital idea! I shall summon the most notable gatherings in the vicinity posthaste! This is *WhatsOn* 🔎")

                    for response in responses:
                        tw.send_message(my_conversation, response)

                else:
                    tw.send_message(my_conversation, responses)

        except ValueError:
            tw.send_message(my_conversation, "Pray, be concise, old sport! 🧐\n(Example: 'berlin tomorrow')")


if __name__ == "__main__":
    main()
