# WhatsOn - WhatsApp Event Discovery Tool

WhatsOn is a WhatsApp-based event discovery tool that helps users find concerts, festivals, and events in their city through WhatsApp. It utilizes Twilio for messaging and integrates external APIs to fetch event details.

## Features
- Uses Twilio for WhatsApp messaging
- Processes user location and event preferences
- Fetches event details based on user input
- Responds with a curated list of events

## Requirements
Ensure you have the following dependencies installed:

```sh
pip install -r requirements.txt
```

**Requirements File (`requirements.txt`):**
```
python-dotenv==1.0.0
twilio==8.4.0
```

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/whatson.git
   cd whatson
   ```
2. Create a `.env` file in the root directory and add your Twilio credentials:
   ```ini
   ACCOUNT_SID=your_account_sid
   AUTH_TOKEN=your_auth_token
   PHONE_NUMBER=your_whatsapp_phone_number
   MS_WHATSAPP_NUMBER=your_messaging_service_whatsapp_number
   ```
3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   python main.py
   ```

## Usage
1. Send a message to the WhatsApp number linked with Twilio.
2. Provide your location and date (e.g., `Berlin tomorrow`).
3. Choose the type of event you are interested in (e.g., `concert`, `sports`, `movie`).
4. Receive a curated list of events based on your preferences.

## Project Structure
```
whatson/
│── main.py                # Main entry point
│── twilio_helpers.py      # Twilio message handling
│── user_input.py          # Processes user location and time input
│── event_extract.py       # Fetches and formats event details
│── store_user_data.py     # Stores user query data
│── store_events.py        # Stores and retrieves event data
│── .env                   # Environment variables (not tracked by Git)
│── requirements.txt       # Project dependencies
```

## Future Enhancements
- Add AI-based event recommendations
- Improve event filtering by user preferences
- Integrate payment services for ticket bookings

## Contributing
Feel free to fork this repository and submit pull requests.

## License
MIT License

