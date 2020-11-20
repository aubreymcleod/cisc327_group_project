# users class test cases by Teaghan Laitar
The users class implements the interactions involving the database and the users that wish to and are currently being stored there.
The test cases will test the different functionalities of the parts of the user class using black box functionallity coverage testing.
The functionallity of the user class (from the comments) will be tested to ensure that all requirements are met.
These have been brocken down in to test cases as follows
| Requirement Name | Requirement | Test Cases|
|------------------|-------------|----------|
|users.1|Given an email the function should return the user if found, and None if not|If the user exists|
| | |If the user does not exist|
|users.2|A user login should be verified with email and password, if both match should return user, if not return None|Correct email and password|
| | |Incorrect password|
| | |Incorrect username|
|users.3|The user should be added to the database when all registration credientals check out, if an error occurs and error should be reported|No unexpected errors|
| | |Unexpected error while running add to the database|
| | |Unexpected error while running commit to the database|


The calls to the database will be patched to return either a test case of user data that would be returned from the data base if the user exists, or None if the user dones not exist.
The calls to save to the data base will also be patched so the test cases do not actually save anything. 

### Test_Data:
	```
	test_user = User(
		email='test_frontend@test.com',
		name='Test_frontend',
		password=generate_password_hash('Pas$word'),
		balance=500000
	)
	```

### Test case users.1.1 - Given an email the function should return the user if found, and None if not [user exists]
	Mocking:
	- Mock `get_user` to return a `test_user` instance
	
	Actions:
	- Set test_email to a valid email (matching the test_user's email)
	- Make a call to get_user() with test_email
	- Validate that the call returns an ins
	
### Test case users.1.2 - Given an email the function should return the user if found, and None if not [user does not exist]
	Mocking:
	- Mock `get_user` to return None
	
	Actions:
	- Set test_email to an invalid email (not the test_user's email)
	- Make a call to get_user() with test_email
	- Validate that the call returns None
	
### Test case users.2.1 - A user login should be verified with email and password, if both match should return user, if not return None [pass]
	Mocking:
	- Mock `get_user` to return a `test_user` instance
	
	Actions:
	- Set test_email to a valid email (matching the test_user's email)
	- Set the test_password to the matching and valid password (matching the test_user's password)
	- Make call to login_user with test_email and test_password
	- Validate that the call returns test user
	
### Test case users.2.2 - A user login should be verified with email and password, if both match should return user, if not return None [fail with non matching password]
	Mocking:
	- Mock `get_user` to return a `test_user` instance
	
	Actions:
	- Set test_email to a valid email (matching the test_user's email)
	- Set the test_password to the non matching and valid password (not the test_user's password)
	- Make call to login_user with test_email and test_password
	- Validate that the call returns None
	
### Test case users.2.3 - A user login should be verified with email and password, if both match should return user, if not return None [fail with non existing user]
	Mocking:
	- Mock `get_user` to return None
	
	Actions:
	- Set test_email to a non valid email (not the test_user's email)
	- Set the test_password to any valid password
	- Make call to login_user with test_email and test_password
	- Validate that the call returns None
	
### Test case users.3.1 - The user should be added to the database when all registration credientals check out, if an error occurs and error should be reported [passing registration]
	Mocking:
	- Mock `db.session.add` to return None
	- Mock `db.session.commit` to return None
	
	Actions:
	- Set test_email to a valid email
	- Set test_name to a valid name
	- Set test_password to a valid password
	- Set test_password2 to a valid and matching password
	- Set test_balance to an interger value
	- Call register_user with all test information
	- Validate that None is returned from the function call
	
### Test case users.3.2 - The user should be added to the database when all registration credientals check out, if an error occurs and error should be reported [Error from .add]
	Mocking:
	- Mock `db.session.add` to return a mocked error
	- Mock `db.session.commit` to return None
	
	Actions:
	- Set test_email to a valid email
	- Set test_name to a valid name
	- Set test_password to a valid password
	- Set test_password2 to a valid and matching password
	- Set test_balance to an interger value
	- Call register_user with all test information
	- Validate that and error is returned from the function call
	
### Test case users.3.3 - The user should be added to the database when all registration credientals check out, if an error occurs and error should be reported [Error from .commit]
	Mocking:
	- Mock `db.session.add` to return None
	- Mock `db.session.commit` to return a mocked error
	
	Actions:
	- Set test_email to a valid email
	- Set test_name to a valid name
	- Set test_password to a valid password
	- Set test_password2 to a valid and matching password
	- Set test_balance to an interger value
	- Call register_user with all test information
	- Validate that and error is returned from the function call