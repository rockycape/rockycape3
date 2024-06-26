import re

def remove_non_chars(text):
    # Capitalize the first letter of each word
    capitalized_text = text.title()
    # The regex pattern [^a-zA-Z] matches any non-letter character.
    pattern = re.compile(r'[^a-zA-Z]')
    cleaned_text = re.sub(pattern, '', capitalized_text)
    return cleaned_text

string = "fantastic-news-for-the-ngt-foundation-establishment-of-the-moore-family-fund"
print(remove_non_chars(string))
