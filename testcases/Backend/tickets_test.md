#tickets class test cases by Melissa Zhu

The tickets class implements the interactions involving the database and the tickets that wish to be added and are currently being stored there.
The test cases will test the different functionalities of the parts of the tickets class using black box functionality coverage testing.
The functionallity of the tickets class (from the comments) will be tested to ensure that all requirements are met.
These have been broken down into test cases as follows
| Requirement Name | Requirement | Test Cases|
|------------------|-------------|----------|
|ticket.1|Given a ticket name the function should return the ticket if found, and None if not|If the ticket exists|
| | |If the ticket does not exist|
|ticket.2|A ticket's expiry date should be verified to be not expired. If ticket is not expired the function should return the ticket, if not return None|Valid date (ticket not expired)|
| | |Invalid date (ticket expired)|
|ticket.3|The ticket should be added to the database when all input requirements check out, if an error occurs it should be reported|No unexpected errors|
| | |Unexpected error while running add to the database|
| | |Unexpected error while running commit to the database|


The calls to the database will be patched to return either a test case of ticket data that would be returned from the data base if the ticket exists, or None if the ticket does not exist.
The calls to save to the data base will also be patched so the test cases do not actually save anything. 

### Test_Data:
	```
	test_ticket = Ticket(
		owner='test_frontend@test.com',
		name='test_ticket_yo',
		quantity=10,
		price=10,
		date='20201231'
	)
	```
### Test case ticket.1.1 - Given a ticket name the function should return the ticket if found, and None if not [ticket exists]
	Mocking:
	- Mock `get_ticket` to return a `test_ticket` instance
	
	Actions:
	- Set test_ticket_name to a valid ticket name (matching the test_ticket's name)
	- Make a call to get_all_tickets() with test_ticket_name
	- Validate that the call returns an instance
	
### Test case ticket.1.2 - Given a ticket name the function should return the ticket if found, and None if not [ticket does not exist]
	Mocking:
	- Mock `get_ticket` to return None
	
	Actions:
	- Set test_ticket_name to an invalid ticket name (not the test_ticket's name)
	- Make a call to get_all_tickets() with test_ticket_name
	- Validate that the call returns None
	
### Test case ticket.2.1 - A ticket's expiry date should be verified to be not expired. If ticket is not expired the function should return the ticket, if not return None [valid]
	Mocking:
	- Mock `get_ticket` to return a `test_ticket` instance
	
	Actions:
	- Set test_ticket_name to a valid ticket name (matching the test_ticket's name)
	- Set the test_ticket_date to a valid date (matching the test_ticket's date)
	- Make call to prune_expired_tickets() with test_ticket_name and test_ticket_date
	- Validate that the call returns test ticket
	
### Test case ticket.2.2 - A ticket's expiry date should be verified to be not expired. If ticket is not expired the function should return the ticket, if not return None [invalid]
	Mocking:
	- Mock `get_ticket` to return None
	
	Actions:
	- Set test_ticket_name to a valid ticket name (matching the test_ticket's name)
	- Set the test_ticket_date to an invalid date (matching the test_ticket's date)
	- Make call to prune_expired_tickets() with test_ticket_name and test_ticket_date
	- Validate that the call returns None

	
### Test case ticket.3.1 - The ticket should be added to the database when all input requirements check out, if an error occurs it should be reported [pass]
	Mocking:
	- Mock `db.session.add` to return None
	- Mock `db.session.commit` to return None
	
	Actions:
	- Set test_ticket_name to a valid ticket name
	- Set test_ticket_owner to a valid ticket owner
	- Set test_ticket_quantity to an integer
	- Set test_ticket_price to an integer
	- Set test_ticket_date to a valid date
	- Call add_ticket() with all test information
	- Validate that None is returned from the function call
	
### Test case ticket.3.2 - The ticket should be added to the database when all input requirements check out, if an error occurs it should be reported [Error from .add]
	Mocking:
	- Mock `db.session.add` to return a mocked error
	- Mock `db.session.commit` to return None
	
	Actions:
	- Set test_ticket_name to a valid ticket name
	- Set test_ticket_owner to a valid ticket owner
	- Set test_ticket_quantity to an integer
	- Set test_ticket_price to an integer
	- Set test_ticket_date to a valid date
	- Call add_ticket() with all test information
	- Validate that and error is returned from the function call
	
### Test case ticket.3.3 - The ticket should be added to the database when all input requirements check out, if an error occurs it should be reported [Error from .commit]
	Mocking:
	- Mock `db.session.add` to return None
	- Mock `db.session.commit` to return a mocked error
	
	Actions:
	- Set test_ticket_name to a valid ticket name
	- Set test_ticket_owner to a valid ticket owner
	- Set test_ticket_quantity to an integer
	- Set test_ticket_price to an integer
	- Set test_ticket_date to a valid date
	- Call add_ticket() with all test information
	- Validate that and error is returned from the function call