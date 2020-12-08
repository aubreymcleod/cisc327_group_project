from email.headerregistry import Address
from datetime import date
import re

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
    #test lengths
    address = email.split('@')
    address[0] = '@'.join(address[:-1])
    if len(address[0])>64 or len(address[-1])>255:
        return False

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



#Ticket validation functions
def validate_ticket(ticket):
	if validate_name(ticket.ticket_name) and validate_date(ticket.ticket_expiration) and validate_quantity(ticket.quantity) and validate_price(ticket.price):
		return True #is valid
	return False

def validate_name(name):
	if re.match("^[a-zA-Z0-9][a-zA-Z0-9 ]*[a-zA-Z0-9]$", name) and 6<=len(name)<=60:
		return True
	return False
	
def validate_date(expiration_date):
	todays_date = date.today().strftime("%Y/%m/%d")
	if re.match("^[0-9][0-9][0-9][0-9](0[1-9]|1[0-2])([0][1-9]|[1-2][0-9]|3[0-1])$", expiration_date) and expiration_date >= todays_date:
		return True
	return False
	
def validate_quantity(qty):
	try:
		if 0<int(qty)<=100:
			return True
	except:
		return False
	return False
	
def validate_price(price):
	try:
		if 10<=int(price)<=100:
			return True
	except:
		return False
	return False
	
