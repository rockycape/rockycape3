# This is a Python script to remove all non-letter characters from a string
import re

def remove_non_chars(text):
    # The regex pattern [^a-zA-Z] matches any non-letter character.
    pattern = re.compile(r'[^a-zA-Z]')
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text

string = "A Short Trip-Thats A Perfect Match For You And Your Bicycle"
print(remove_non_chars(string))