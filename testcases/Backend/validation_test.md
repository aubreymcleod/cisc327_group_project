# validation class test cases by Aubrey McLeod
The validation class implements a set of input validation methods which define what inputs are and are not allowed in a given field.
These test cases will test the email and password validation using black box functionallity coverage testing.
The functionallity of the user class (from the comments) will be tested to ensure that all requirements are met.
These have been brocken down in to test cases as follows
| Requirement Name | Requirement | Test Cases|
|------------------|-------------|----------|
|email|emails must conform to RFC5322| has a valid standard-form local address |
| | | has a standard-form local address, but contains double dots |
| | | has a standard-form local address, but starts with a dot |
| | | has a standard-form local address, but ends with a dot |
| | | has a valid quoted-form local address |
| | | has an invalid quoted-form local address |
| | | has a valid local address and a valid standard form domain |
| | | has a valid local address and an invalid standard form domain |
| | | has a valid local address and an IPv4 domain |
| | | has a valid local address and an IPv6 domain |
| | | has an invalid structure (no @) |
| | | has an invalid structure (multiple unquoted @) |
| | | has an invalid structure (invalid characters outside of quotes) |
| | | has an invalid structure (quotes in wrong place) |
| | | has an invalid structure (quotes in wrong place) |
| | | has an invalid structure (too long) |
| | | |
|password| passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character | >6(1), special(1), upper(1), lower(1) |
| | | >6(0), special(1), upper(1), lower(1) |
| | | >6(1), special(0), upper(1), lower(1) |
| | | >6(0), special(0), upper(1), lower(1) |
| | | >6(1), special(1), upper(0), lower(1) |
| | | >6(0), special(1), upper(0), lower(1) |
| | | >6(1), special(0), upper(0), lower(1) |
| | | >6(0), special(0), upper(0), lower(1) |
| | | >6(1), special(1), upper(1), lower(0) |
| | | >6(0), special(1), upper(1), lower(0) |
| | | >6(1), special(0), upper(1), lower(0) |
| | | >6(0), special(0), upper(1), lower(0) |
| | | >6(1), special(1), upper(0), lower(0) |
| | | >6(0), special(1), upper(0), lower(0) |
| | | has none of the valid characters, but long enough to meet the 6 char requirements |
| | | has none of the valid characters and too short |


The calls to the database will be patched to return either a test case of user data that would be returned from the data base if the user exists, or None if the user dones not exist.
The calls to save to the data base will also be patched so the test cases do not actually save anything. 


### EMAIL.1 - emails must conform to RFC5322, standard local address -> True
	Actions:
	- Set test_email to "test_01@test.com"
	- Make a call to validate_email_address() with test_email
	- Validate that the call returns True
	
### EMAIL.2 - emails must conform to RFC5322, double dot standard local address -> false
	Actions:
	- Set test_email to "test..02@test.com"
	- Make a call to validate_email_address() with test_email
	- Validate that the call returns False
	
### EMAIL.3 - emails must conform to RFC5322, dot start standard local address -> false
	Actions:
	- Set test_email to ".test.03@test.com"
	- Make a call to validate_email_address() with test_email
	- Validate that the call returns False
	
### EMAIL.4 - emails must conform to RFC5322, dot end standard local address -> false
	Actions:
	- Set test_email to "test.04.@test.com"
	- Make a call to validate_email_address() with test_email
	- Validate that the call returns False
	
### EMAIL.5 - emails must conform to RFC5322, quoted local address -> true
	Actions:
	- Set test_email to "\"test..05\"@test.com"
	- Make a call to validate_email_address() with test_email
	- Validate that the call returns True
	
### EMAIL.6 - emails must conform to RFC5322, quoted local address invalid -> false
	Actions:
	- Set test_email to '\"test06\\\"@test.com'
	- Make a call to validate_email_address() with test_email
	- Validate that the call returns False
	
### EMAIL.7 - emails must conform to RFC5322, valid domain -> True
	Actions:
	- Set test_email to 'test_07@test.com'
	- Make a call to validate_email_address() with test_email
	- Validate that the call returns True
	
### EMAIL.8 - emails must conform to RFC5322, invalid domain -> False
	Actions:
	- Set test_email to 'test_08@'
	- Make a call to validate_email_address() with test_email
	- Validate that the call returns False
	
### EMAIL.9 - emails must conform to RFC5322, domain ip4 -> True
	Actions:
	- Set test_email to 'test_09@[127.0.0.1]'
	- Make a call to validate_email_address() with test_email
	- Validate that the call returns True
	
### EMAIL.10 - emails must conform to RFC5322, domain ipv6 -> True
	Actions:
	- Set test_email to 'test_10@[IPv6:2001:db8::1]'
	- Make a call to validate_email_address() with test_email
	- Validate that the call returns True
	
### EMAIL.11 - emails must conform to RFC5322, invalid structure no @ = False
	Actions:
	- Set test_email to 'test.11.com'
	- Make a call to validate_email_address() with test_email
	- Validate that the call returns False
	
### EMAIL.12 - emails must conform to RFC5322, invalid structure = False
	Actions:
	- Set test_email to 't@e@s@t@12.test.com'
	- Make a call to validate_email_address() with test_email
	- Validate that the call returns False

### EMAIL.13 - emails must conform to RFC5322, bad chars out of quotes = False
	Actions:
	- Set test_email to 'a\"\\ b(c)d,e:f;g<h>i[j\\k]l@example.com'
	- Make a call to validate_email_address() with test_email
	- Validate that the call returns False
	
### EMAIL.14 - emails must conform to RFC5322, bad quote placement = False
	Actions:
	- Set test_email to 'just"not"right@example.com'
	- Make a call to validate_email_address() with test_email
	- Validate that the call returns False
	
### EMAIL.15 - emails must conform to RFC5322, local too long = False
	Actions:
	- Set test_email to '1234567890123456789012345678901234567890123456789012345678901234+x@example.com'
	- Make a call to validate_email_address() with test_email
	- Validate that the call returns False
	
	
	
### PW.1 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(1), special(1), upper(1), lower(1) => True
	Actions:
	- Set test_password to 'Valid_Password'
	- Make a call to validate_password() with test_password
	- Validate that the call returns True
	
### PW.2 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(0), special(1), upper(1), lower(1) => False
	Actions:
	- Set test_password to 'In_'
	- Make a call to validate_password() with test_password
	- Validate that the call returns False
	
### PW.3 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(1), special(0), upper(1), lower(1) => False
	Actions:
	- Set test_password to 'InvalidPassword'
	- Make a call to validate_password() with test_password
	- Validate that the call returns False
	
### PW.4 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(0), special(0), upper(1), lower(1) => False
	Actions:
	- Set test_password to 'Inval'
	- Make a call to validate_password() with test_password
	- Validate that the call returns False
	
### PW.5 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(1), special(1), upper(0), lower(1) => False
	Actions:
	- Set test_password to 'invalid_password'
	- Make a call to validate_password() with test_password
	- Validate that the call returns False
	
### PW.6 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(0), special(1), upper(0), lower(1) => False
	Actions:
	- Set test_password to 'inva_'
	- Make a call to validate_password() with test_password
	- Validate that the call returns False
	
### PW.7 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(1), special(0), upper(0), lower(1) => False
	Actions:
	- Set test_password to 'invalidpassword'
	- Make a call to validate_password() with test_password
	- Validate that the call returns False
	
### PW.8 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(0), special(0), upper(0), lower(1) => False
	Actions:
	- Set test_password to 'inval'
	- Make a call to validate_password() with test_password
	- Validate that the call returns False
	
### PW.9 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(1), special(1), upper(1), lower(0) => False
	Actions:
	- Set test_password to 'INVALID_PASSWORD'
	- Make a call to validate_password() with test_password
	- Validate that the call returns False
	
### PW.10 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(0), special(1), upper(1), lower(0) => False
	Actions:
	- Set test_password to 'INVA_'
	- Make a call to validate_password() with test_password
	- Validate that the call returns False
	
### PW.11 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(1), special(0), upper(1), lower(0) => False
	Actions:
	- Set test_password to 'INVALIDPASSWORD'
	- Make a call to validate_password() with test_password
	- Validate that the call returns False
	
### PW.12 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(0), special(0), upper(1), lower(0) => False
	Actions:
	- Set test_password to 'INVAL'
	- Make a call to validate_password() with test_password
	- Validate that the call returns False

### PW.13 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(1), special(1), upper(0), lower(0) => False
	Actions:
	- Set test_password to '______'
	- Make a call to validate_password() with test_password
	- Validate that the call returns False
	
### PW.14 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(0), special(1), upper(0), lower(0) => False
	Actions:
	- Set test_password to '_'
	- Make a call to validate_password() with test_password
	- Validate that the call returns False
	
### PW.15 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - test: >6(0), special(0), upper(0), lower(0) => False
	Actions:
	- Set test_password to ''
	- Make a call to validate_password() with test_password
	- Validate that the call returns False
	
### PW.16 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - invalid characters short => False
	Actions:
	- Set test_password to '\0\0\0\0\0\0'
	- Make a call to validate_password() with test_password
	- Validate that the call returns False
	
### PW.17 - passwords must be of length 6 or greater, contain one special character, one upper case character, one lowercase character - invalid characters short => False
	Actions:
	- Set test_password to '\0\0\0'
	- Make a call to validate_password() with test_password
	- Validate that the call returns False