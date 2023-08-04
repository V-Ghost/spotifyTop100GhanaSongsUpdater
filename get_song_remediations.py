import re

def extract_words_from_string(string):
    words = string.split(',')
    words = [word.strip() for word in words]  # Remove leading/trailing whitespaces
    return words



def split_case_string(string):
    words = re.findall('[A-Z][a-z]*', string)
    result = ""
    for word in words:
        result = result + " " +word 
    return result

# Example usage

