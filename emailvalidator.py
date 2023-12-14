import re

def validate_email(email):
    # Regular expression for a basic email validation
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    # Use the match method to check if the email matches the pattern
    if pattern.match(email):
        return True
    else:
        return False

# Example usage
email_to_check = input("Enter an email address: ")

if validate_email(email_to_check):
    print("Valid email address")
else:
    print("Invalid email address")
