import re

def validate_values(number):
        regex = "^[-+]?[0-9]*(.[0-9]{1,2})?$"
        match = re.match(regex, number)
        return match is not None