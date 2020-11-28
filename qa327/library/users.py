from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines any and all functions for operating on users:
- accessing users profiles by their emails
- login in a user to a new session
- registering new users
- etc.
"""

def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user


def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    """
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def register_user(email, name, password, password2, balance):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :param balance: an integer value of user balance in cents
    :return: an error message if there is any, or None if register succeeds
    """

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    new_user = User(email=email, name=name, password=hashed_pw, balance=balance)
    try:
        db.session.add(new_user)
        db.session.commit()
        return None
    except:
        return 'error'
    

def reduce_balance(email, cost):
    """
    This function updates the balance in the database after tickets are successfully purchased.
    """
    user = get_user(email)
    user.balance = user.balance - (cost * 100)
    db.session.commit()
    return None
    

    
