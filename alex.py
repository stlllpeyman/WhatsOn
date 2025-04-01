import dateparser
import re
import spacy
from pydantic.v1.datetime_parse import parse_date

nlp = spacy.load('en_core_web_sm')

def extract_location(user_message):
    """Takes user message and processes using nlp module of spaCy"""
    doc = nlp(user_message)
    for ent in doc.ents:
        if ent.label_ in ["GPE", "LOC"]: # GPE = Geopolitical entity Loc = known location.
            location = ent.text # we may need another step if we need to convert the format
            return location
        else:
            return None # If no location found

def extract_multi_locations(user_message):
    """As extract_location but returns list of locations inc multi-word"""
    doc = nlp(user_message)
    locations = [] # initiates a list to store extracted places
    combined_location = []

    #print([(ent.text, ent.label_) for ent in doc.ents])
    for ent in doc.ents:
        if ent.label_ in["GPE", "LOC"]:
            locations.append(ent.text.strip())
            if combined_location:
                combined_location.append(ent.text)
                locations.append(" ".join(combined_location))

    return locations


def extract_date(user_message):
    parsed_date = dateparser.parse(user_message)
    if parsed_date:
        return parsed_date.strftime("%Y-%m-%d") # we will probably need to adjust based on API reqs
    return None

def clean_location_and_date(user_message):
    location = extract_location(user_message)
    date = extract_date(user_message)
    return f"{location}, {date}" # we can either format here or in the JSON?




# These messages possibly need adding to the main function?
# def handle_invalid_location():
#    return "Hmmm, we didn't recognize that location. Try a clear name like... 'London' or 'Edinburgh Castle'"

# def handle_invalid_date():
#    return "Hmm, we didn't recognize that date. Try something like... 'April 10, 2025' or 'next Monday'."


print(clean_location_and_date("I want to visit Warwick, 10th march"))
print(extract_multi_locations("I want to visit Warwick Castle"))


