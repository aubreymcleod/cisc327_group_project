from email.headerregistry import Address

"""
This file defines all calls needed to validate UI fields on the
backend, such as email format validation and password format validation.
"""

def validate_email_address(email):
    """
    ensure that given email meets RFC 5322 standards,
    here we pass the email to the Address object from the headerregistry library.
    :param email: the email of the user
    :return: returns True if the email is valid, False otherwise
    """
    try:
        Address(addr_spec=email)
        return True
    except:
        return False

def validate_password(password):
    """
    ensure that any input password is at least length 6, has at least one upper case,
    at least one lower case, and at least one special character
    :param password: the password of the user
    :return: returns True if the password is valid, False otherwise
    """
    special_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    has_uppercase = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(special_char in special_chars for special_char in password)
    if len(password)>=6 and has_lower and has_uppercase and has_special:
        return True
    return False