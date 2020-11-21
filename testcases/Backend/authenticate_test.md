# authenticate class test cases by Nicole Osayande

The authenticate class authenticates a users session. This ensures that any 
logged-in only routes are accessible to valid users (we redirect
unauthorized visitors to the login page otherwise)

The test cases will test the different functionalities of the parts of the authenticate class using black box functionality coverage testing.

Breakdown:
| Requirement Name | Requirement | Test Cases|
|------------------|-------------|----------|
|authenticate.1|Given any python function that accepts a user object, should return inner_function(user) if logged in, or redirect to the login page otherwise|logged in session|
| | |not logged in|

The calls to the database will be patched to return either a test case of user data that would be returned from the data base if the user exists, or None if the user dones not exist. The calls to save to the data base will also be patched so the test cases do not actually save anything.

### Test_Data:
	```
	test_user = User(
		email='test_frontend@test.com',
		name='Test_frontend',
		password=generate_password_hash('Pas$word'),
		balance=500000
	)
	```

### Test case authenticate.1.1 - Given any python function that accepts a user object, should return inner_function(user) if logged in, or redirect to the login page otherwise [logged in session]
	Mocking:
	- Mock 'authenticate(inner_function)' to wrap inner_function
	- Mock 'wrapped_inner' to return return inner_function(user)
	- Mock `get_user` to return a `test_user` instance

	Actions:
	- set 'email' to a 'logged in' session for a valid user
	- Make a call to get_user() with 'email'
	- Validate that the inner_function(user) is returned

### Test case authenticate.1.2 - Given any python function that accepts a user object, should return inner_function(user) if logged in, or redirect to the login page otherwise [logged out]
	Mocking:
	- Mock 'authenticate(inner_function)' to wrap inner_function
	- Mock 'wrapped_inner' to return redirect('/login')
	- Mock `get_user` to return a `test_user` instance

	Actions:
	- Check that 'logged in' is not in 'session'
	- Validate that redirect('/login') is returned