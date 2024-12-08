import re


# Validation functions
def validate_email(value):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", value) is not None

def validate_phone(value):
    return re.match(r"^\+7\d{10}$", value) is not None

def validate_date(value):
    return re.match(r"^(\d{4}-\d{2}-\d{2}|\d{2}\.\d{2}\.\d{4})$", value) is not None

def determine_field_type(value):
    if validate_date(value):
        return "date"
    elif validate_phone(value):
        return "phone"
    elif validate_email(value): 
        return "email"
    else:
        return "text"

