
import spacy


nlp = spacy.load('en_core_web_sm')

def extract_location(user_message):
    """Takes user message and processes using nlp module of spaCy"""
    doc = nlp(user_message)
    for ent in doc.ents:
        if ent.label_ in ["GPE", "LOC"]: # GPE = Geopolitical entity, Loc = known location.
            location = ent.text # we may need another step if we need to convert the format
            return location

    return None # If no location found


def extract_date(user_message):
    """Takes user message and processes using nlp module of spaCy"""
    doc = nlp(user_message)
    for ent in doc.ents:
        if ent.label_ in ["DATE"]:
            date = ent.text  # we may need another step if we need to convert the format
            return date
    return None  # If no location




def clean_location_and_date(user_message):
    location = extract_location(user_message)
    date = extract_date(user_message)
    return location, date # we can either format here or in the JSON?


print(clean_location_and_date("Los Angeles tomorrow"))
print(clean_location_and_date("Neverland next week"))
print(clean_location_and_date("London Any"))
print(clean_location_and_date("Camden Town today"))
print(clean_location_and_date(" next week"))
print(clean_location_and_date("Camden Town"))
print(clean_location_and_date(" next week"))

#

