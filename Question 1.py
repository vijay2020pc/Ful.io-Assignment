import re

def validate_contact_number(number):
    # Regular expression pattern for matching various contact number formats
    pattern = r'^(\+\d{1,2})?[\s\(\.-]*\d{3}[\s\)\.-]*\d{3}[\s\.-]*\d{4}$'
    
    if re.match(pattern, number):
        return True
    else:
        return False

# List of contact numbers in different formats
number = input()

# Validate and print the status for each contact number

if validate_contact_number(number):
    print(f"{number} is a valid contact number.")
else:
    print(f"{number} is an invalid contact number.")
