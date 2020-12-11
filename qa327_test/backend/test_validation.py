import pytest

import qa327.library.validation as valid

"""
This file defines all unit tests for the backend validation functions.
"""
### Email validation
# emails must meet the RFC5322 standard
# must contain a @
# Emails must have two parts, the local address <= 64 in length, and the domain <=255
# local address must either be alphanumeric with '.' (not at start or end or next to any other dots) or any of the following '!#$%&'*+-/=?^_`{|}~', and have a length greater than 0 but less than 64
# local address may also be encapsulated in double quotes, which allows for any valid printable character, with some exceptions.
# domains must be alpha numeric with options for - (not at the end), with '.' acting as a separator.
# domains may take the form of an ip4 address (contained in '[]') or ipv6, contained in '[]'


# EMAIL.1 - emails must conform to RFC5322, standard local address -> True
def test_validation_email_valid_email_std():
    test_email = 'test_01@test.com'
    assert valid.validate_email_address(test_email) is True


# EMAIL.2 - emails must conform to RFC5322, double dot standard local address -> false
def test_validation_email_invalid_email_std_ddot():
    test_email = 'test..02@test.com'
    assert valid.validate_email_address(test_email) is False


# EMAIL.3 - emails must conform to RFC5322, dot start standard local address -> false
def test_validation_email_invalid_email_std_dstart():
    test_email = '.test.03@test.com'
    assert valid.validate_email_address(test_email) is False


# EMAIL.4 - emails must conform to RFC5322, dot end standard local address -> false
def test_validation_email_invalid_email_std_dend():
    test_email = 'test.04.@test.com'
    assert valid.validate_email_address(test_email) is False


# EMAIL.5 - emails must conform to RFC5322, quoted local address -> true
def test_validation_email_valid_email_quotes():
    test_email = '\"test..05\"@test.com'
    assert valid.validate_email_address(test_email) is True


# EMAIL.6 - emails must conform to RFC5322, quoted local address invalid -> false
def test_validation_email_invalid_email_quotes():
    test_email = '\"test06\\\"@test.com'
    assert valid.validate_email_address(test_email) is False

# EMAIL.7 - emails must conform to RFC5322, valid domain -> True
def test_validation_email_valid_email_domain():
    test_email = 'test_07@test.com'
    assert valid.validate_email_address(test_email) is True

# EMAIL.8 - emails must conform to RFC5322, invalid domain -> False
def test_validation_email_invalid_email_domain():
    test_email = 'test_08@'
    assert valid.validate_email_address(test_email) is False

# EMAIL.9 - emails must conform to RFC5322, domain ip4 -> True
def test_validation_email_valid_email_domain_ip4():
    test_email = 'test_09@[127.0.0.1]'
    assert valid.validate_email_address(test_email) is True

# EMAIL.10- emails must conform to RFC5322, domain ipv6 -> True
def test_validation_email_valid_email_domain_ipv6():
    test_email = 'test_10@[IPv6:2001:db8::1]'
    assert valid.validate_email_address(test_email) is True

# EMAIL.11- emails must conform to RFC5322, invalid structure no @ = False
def test_validation_email_invalid_structure_no_at():
    test_email = 'test.11.com'
    assert valid.validate_email_address(test_email) is False

# EMAIL.12- emails must conform to RFC5322, invalid structure = False
def test_validation_email_invalid_structure_too_many_ats():
    test_email = 't@e@s@t@12.test.com'
    assert valid.validate_email_address(test_email) is False

# EMAIL.13- emails must conform to RFC5322, bad chars out of quotes = False
def test_validation_email_invalid_character_placement():
    test_email = 'a\"\\ b(c)d,e:f;g<h>i[j\\k]l@example.com'
    assert valid.validate_email_address(test_email) is False

# EMAIL.14- emails must conform to RFC5322, bad quote placement = False
def test_validation_email_invalid_quote_placement():
    test_email = 'just"not"right@example.com'
    assert valid.validate_email_address(test_email) is False

# EMAIL.15- emails must conform to RFC5322, local too long = False
def test_validation_email_long_local():
    test_email = '1234567890123456789012345678901234567890123456789012345678901234+x@example.com'
    assert valid.validate_email_address(test_email) is False

###Password Validation
# passwords must be of length 6 or greater.
# passwords must contain one special character
# passwords must contain one upper case character
# passwords must contain one lower case character


# PW.1 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(1), special(1), upper(1), lower(1) => True
def test_validation_password_valid_password():
    test_password = 'Valid_Password'
    assert valid.validate_password(test_password) is True


# PW.2 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(0), special(1), upper(1), lower(1) => False
def test_validation_password_invalid_short_password():
    test_password = 'In_'
    assert valid.validate_password(test_password) is False


# PW.3 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(1), special(0), upper(1), lower(1) => False
def test_validation_password_invalid_short_password():
    test_password = 'InvalidPassword'
    assert valid.validate_password(test_password) is False


# PW.4 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(0), special(0), upper(1), lower(1) => False
def test_validation_password_invalid_short_no_spec_password():
    test_password = 'Inval'
    assert valid.validate_password(test_password) is False


# PW.5 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(1), special(1), upper(0), lower(1) => False
def test_validation_password_invalid_lowercase_password():
    test_password = 'invalid_password'
    assert valid.validate_password(test_password) is False


# PW.6 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(0), special(1), upper(0), lower(1) => False
def test_validation_password_invalid_short_lowercase_password():
    test_password = 'inva_'
    assert valid.validate_password(test_password) is False


# PW.7 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(1), special(0), upper(0), lower(1) => False
def test_validation_password_invalid_no_special_and_lowercase_password():
    test_password = 'invalidpassword'
    assert valid.validate_password(test_password) is False


# PW.8 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(0), special(0), upper(0), lower(1) => False
def test_validation_password_invalid_short_no_special_and_lowercase_password():
    test_password = 'inval'
    assert valid.validate_password(test_password) is False


# PW.9 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(1), special(1), upper(1), lower(0) => False
def test_validation_password_invalid_no_lower():
    test_password = 'INVALID_PASSWORD'
    assert valid.validate_password(test_password) is False


# PW.10 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(0), special(1), upper(1), lower(0) => False
def test_validation_password_invalid_short_no_lower():
    test_password = 'INVA_'
    assert valid.validate_password(test_password) is False


# PW.11 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(1), special(0), upper(1), lower(0) => False
def test_validation_password_invalid_no_special_and_no_lower():
    test_password = 'INVALIDPASSWORD'
    assert valid.validate_password(test_password) is False


# PW.12 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(0), special(0), upper(1), lower(0) => False
def test_validation_password_invalid_short_no_special_and_no_lower():
    test_password = 'INVAL'
    assert valid.validate_password(test_password) is False


# PW.13 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(1), special(1), upper(0), lower(0) => False
def test_validation_password_invalid_special_only():
    test_password = '______'
    assert valid.validate_password(test_password) is False


# PW.14 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(0), special(1), upper(0), lower(0) => False
def test_validation_password_invalid_short_special_only():
    test_password = '_'
    assert valid.validate_password(test_password) is False

# PW.15 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(0), special(0), upper(0), lower(0) => False
def test_validation_password_empty():
    test_password = ''
    assert valid.validate_password(test_password) is False

# PW.16 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - invalid characters short => False
def test_validation_password_invalid_chars_():
    test_password = '\0\0\0\0\0\0'
    assert valid.validate_password(test_password) is False

# PW.17 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - invalid characters short => False
def test_validation_password_invalid_chars_():
    test_password = '\0\0\0'
    assert valid.validate_password(test_password) is False


# TICKET VALIDATION #

# VALIDATE NAME - Test Cases (based on the 2 branches)
# Match Regex   6=<len<=60  Outcome     Branch  TestValues              CASE
# 0             0           FALSE       1       "@"                     1
# 0             1           FALSE       1       "@@@@@@"                2
# 1             0           FALSE       1       "a"                     3
# 1             1           TRUE        2       "aaaaaa"                4

# NAME.1
def test_validation_name_nomatch_tooshort():
    test_name = "@"
    assert valid.validate_name(test_name) is False

# NAME.2
def test_validation_name_nomatch():
    test_name = "@@@@@@"
    assert valid.validate_name(test_name) is False

# NAME.3
def test_validation_name_tooshort():
    test_name = "a"
    assert valid.validate_name(test_name) is False

# NAME.4
def test_validation_name_valid():
    test_name = "aaaaaa"
    assert valid.validate_name(test_name) is True

# VALIDATE DATE - Test Cases (based on the 2 branches)
# Match Regex   Outcome     Branch  TestValues              CASE
# 0             FALSE       1       "00000000"              1
# 1             FALSE       1       "19700101"              3

# DATE.1
def test_validation_date_nomatch_expired():
    test_date = "00000000"
    assert valid.validate_date(test_date) is False

# DATE.2
def test_validation_date_nomatch():
    test_date = "20213112"
    assert valid.validate_date(test_date) is True



# VALIDATE EXPIRED - Test Cases (based on the 2 branches)
# Match Regex   Date>Today  Outcome     Branch  TestValues              CASE
# 0             0           FALSE       1       "00000000"              1
# 0             1           FALSE       1       "20213112"              2
# 1             0           FALSE       1       "19700101"              3
# 1             1           TRUE        2       "20201231"              4

# EXPIRED.1
def test_validation_expiery_nomatch_expired():
    test_date = "00000000"
    assert valid.validate_not_expired(test_date) is False

# EXPIRED.2
def test_validation_expiery_nomatch():
    test_date = "20213112"
    assert valid.validate_not_expired(test_date) is False

# EXPIRED.3
def test_validation_expiery_expired():
    test_date = "19700101"
    assert valid.validate_not_expired(test_date) is False

# EXPIRED.4
def test_validation_expiery_valid():
    test_date = "20201231"
    assert valid.validate_not_expired(test_date) is True

# VALIDATE QTY - Test Cases (based on the 2 branches)
# Valid Int     0<qty<=100  Outcome     Branch  TestValues              CASE
# 0             0           FALSE       2       "zero"                1
# 0             1           FALSE       2       "1E"                    2
# 1             0           FALSE       3       "0"                     3
# 1             1           TRUE        1       "1"                     4

# QTY.1
def test_validation_qty_badint_outofrange():
    test_qty = "zero"
    assert valid.validate_quantity(test_qty) is False

# QTY.2
def test_validation_qty_badint_inrange():
    test_qty = "1E"
    assert valid.validate_quantity(test_qty) is False

# QTY.3
def test_validation_qty_outofrange():
    test_qty = "0"
    assert valid.validate_quantity(test_qty) is False

# QTY.4
def test_validation_qty_valid():
    test_qty = "1"
    assert valid.validate_quantity(test_qty) is True

# VALIDATE PRICE - Test Cases (based on the 2 branches)
# Valid Int     0<prc<=100  Outcome     Branch  TestValues              CASE
# 0             0           FALSE       2       "MILLION"                1
# 0             1           FALSE       2       "1E"                    2
# 1             0           FALSE       3       "9"                     3
# 1             1           TRUE        1       "10"                    4

# QTY.1
def test_validation_price_badint_outofrange():
    test_price = "MILLION"
    assert valid.validate_price(test_price) is False

# QTY.2
def test_validation_price_badint_inrange():
    test_price = "1E"
    assert valid.validate_price(test_price) is False

# QTY.3
def test_validation_price_outofrange():
    test_price = "9"
    assert valid.validate_price(test_price) is False

# QTY.4
def test_validation_price_valid():
    test_price = "10"
    assert valid.validate_price(test_price) is True