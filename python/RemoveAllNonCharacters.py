# This is a Python script to remove all non-letter characters from a string
import re

def remove_non_chars(text):
    # The regex pattern [^a-zA-Z] matches any non-letter character.
    pattern = re.compile(r'[^a-zA-Z]')
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text

string = "Scam, Sleep And Scam Again. Inside The Scam Facility Behind Those Annoying Text Messages - Abc News"
print(remove_non_chars(string))