# SeetGeek Assignment 5 - Failure Report
  
###Section 1: Aubrey McLeod
  
#####Front End Test Implementation Failures
  
|Feature Specification|Sub-Section|Sub-Section Description|Problem|Resolution|
|---------------------|-----------|-----------------------|-------|----------|
|R4|4.1.1| The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. (pass) | Predicted Success Message differed from actual code.| Reformatted test message, to match code. |
| |4.1.2-4.1.8| The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. (fail) |Predicted Failure Message differed from actual code. | Reformatted test message, to match code. |
| |4.2.1| The name of the ticket is no longer than 60 characters. (pass) | Predicted Success Message differed from actual code.| Reformatted test message, to match code. |
| |4.2.2| The name of the ticket is no longer than 60 characters. (fail) | Predicted Failure Message differed from actual code.| Reformatted test message, to match code. |
| |4.3.1-4.3.3| The quantity of the tickets has to be more than 0, and less than or equal to 100. (pass) | Predicted Success Message differed from actual code.| Reformatted test message, to match code. |
| |4.3.4-4.3.6| The quantity of the tickets has to be more than 0, and less than or equal to 100. (fail) | Predicted Failure Message differed from actual code.| Reformatted test message, to match code. |
| |4.3.7| The quantity of the tickets has to be more than 0, and less than or equal to 100.(fail due to blank field) | Does not fall under scope of front-end test, because blank submission is a homepage test.| Removed test case. |
| |4.4.1-4.4.2| Price has to be of range [10, 100] (pass) | Predicted Success Message differed from actual code.| Reformatted test message, to match code. |
| |4.4.3-4.4.5| Price has to be of range [10, 100] (fail) | Predicted Failure Message differed from actual code.| Reformatted test message, to match code. |
| |4.4.6| Price has to be of range [10, 100] (fail due to blank field) | Does not fall under scope of front-end test, because blank submission is a homepage test.| Removed test case. |
| |4.5.1| Date must be given in the format YYYYMMDD (e.g. 20200901) (pass) | Predicted Success Message differed from actual code.| Reformatted test message, to match code. |
| |4.5.2-4.5.4| Date must be given in the format YYYYMMDD (e.g. 20200901) (fail) | Predicted Failure Message differed from actual code.| Reformatted test message, to match code. |
| |4.5.5| Date must be given in the format YYYYMMDD (e.g. 20200901) (failure due to blank field) | Does not fall under scope of front-end test, because blank submission is a homepage test.| Removed test case. |
| |4.6| For any errors, redirect back to / and show an error message | Error message did not match code| revised test message. |
| | 4.7 | The added new ticket information will be posted on the user profile page | This is actually an integration test | Not implemented because it is out of scope. |
| | 4.8.1 | The name of the ticket must be at least 6 characters long (pass) | Predicted Success Message differed from actual code. | Reformatted test message, to match code. |
| | 4.8.2 | The name of the ticket must be at least 6 characters long (fail due to blank field) | Originally called for blank field, which is not possible through the front end, currently | Refactored test 4.8.3 into this slot |
| | 4.8.3 | The name of the ticket must be at least 6 characters long (fail due to being too short) | Redundant due to refactoring into test 4.8.2 | removed original test case in this position. |
| | 4.9 | The ticket(s) must not be expired |  Error message did not match code| revised test message.|
  
  
#####Backend Test Implementation Failures
No failures were encountered when implementing whitebox tests for: `validate_name()`, `validate_date()`, `validate_quantity()`, or `validate_price()`.



###Section 2: Teaghan Laitar

I implemented the test set from A1 for features R6. I also added to the test_user.py backend test cases.

For the test implementation of R6 the most noticeable failures were in design of the test cases. These have been grouped together for ease in the failure table bellow.
A lot of the test cases had elements that do not exist so they had to be changed. Also the entry data in each test case did not reflect what was being tested.
For more information on the individual test cases see R6.md in the test cases folder of our project.

For the backend I added test cases for the reduce_balance function since it was not created when the backend tests for this file were originally made.
For more information on the individualtest cases for the user class see the backend tests in the test cases folder of out project.

#####Front End Test Implementation Failures
|Feature Specification|Sub-Section|Sub-Section Description|Problem|Resolution|
|---------------------|-----------|-----------------------|-------|----------|
|R6| Test Data | Test data the will be used for the test cases | Contained unneccessary and incorrect values | Made adjustments so the test data is used properly |
||All| Test the ability to buy tickets with a variety of good and bad user input. | The plain language test cases all involved inserting data into slots on the form that do not exist. | Changed test case so data is only entered into existing spot on the from. |
||All| Test the ability to buy tickets with a variety of good and bad user input. | The plain language test cases all called to be backend to buy tickets. | Added a pactch to the test cases. |
||All| Test the ability to buy tickets with a variety of good and bad user input. | The plain language test cases did not change the input to match the test case described. | Changed the mocked user input in the test cases. |
||All| Test the ability to buy tickets with a variety of good and bad user input. | The plain language test cases error message checks no longer match the output from the code. | Made the checks for the correct error message. |
||2.3| Does not exist | Since the creation of the test cases we have added the requirement that ticket names be 6 or more characters, so this is not checked for | Added test case. |
||2.4| Does not exist | There is no check for a passing name length of 6, the boundary case | Added a test fro a name length of 6 |
||2.5| Does not exist | There is no check for a passing name length of 60, the boundary case | Added a test fro a name length of 60 |
||3.5| Test alphabetical entries into the quantity field. | Test fails, no error message is shown. | Added a condition to the buy.py to check that the entries in quantity are numbers. |
||3.1, 2, 4| Test valid quanitiy entries. | After the last fix all entries failed. | Had to change an == to a != |
||4.3| Does not exist | No test for if the ticket is not found | Added test for if the ticket is not found |
||6.1| Test redirection and error message if an error occurs | The redirection was not included in the test case | Added redirection confirmation to the test case |
||6.1| Test redirection and error message if an error occurs | The error message check did not match the displayed error message after changes were made in the most recent merge | Changed the required error message |
||1.1| Tests successful purchase of tickets | The error message check did not match the displayed error message after changes to spelling were made in the most recent push | Changed the checked error message to match |
||2.1, 2.4, 2.5| Tests successful purchase of tickets | The error message check did not match the displayed error message after changes to spelling were made in the most recent push | Changed the checked error message to match |
||3.1-2| Tests successful purchase of tickets | The error message check did not match the displayed error message after changes to spelling were made in the most recent push | Changed the checked error message to match |
||4.1| Tests successful purchase of tickets | The error message check did not match the displayed error message after changes to spelling were made in the most recent push | Changed the checked error message to match |
||5.1| Tests successful purchase of tickets | The error message check did not match the displayed error message after changes to spelling were made in the most recent push | Changed the checked error message to match |

#####Back End Test Implementation Failures
|Feature Specification|Sub-Section|Sub-Section Description|Problem|Resolution|
|---------------------|-----------|-----------------------|-------|----------|
|USER|reduce_balance| Test the ability to reduce the user balance | Test came back as a failure because the user did not exist | Added a patch to mock the get_user |



## Section 3 by Nicole Osayande - I implemented test cases for the first half of R5 and made a few changes to the error messages in update.py file

##Front End Test Implementation Failures
|Feature Specification|Sub-Section|Sub-Section Description|Problem|Resolution|
|---------------------|-----------|-----------------------|-------|----------|
|R5|1.2|name of the ticket has to be alphanumeric-only, and space allowed on if it is not the first or the last character|error message not visible after six seconds|change the error message to match error message in update.py|
||2.2|name of the ticket is no longer than 60 characters [fail]|type syntax error|enter name in string format|
||3.1|quantity of the tickets has to be more than 0, and less than or equal to 100 [pass]|message not visible after six seconds|change the id's to match the index file|


#####Section 4: Melissa Zhu

I implemented the test set from A1 for features R5.4 to R5.7 as well as the backend test cases for tickets.

#####Front End Test Implementation Failures
|Feature Specification|Sub-Section|Sub-Section Description|Problem|Resolution|
|---------------------|-----------|-----------------------|-------|----------|
|R5|5.4.6| Price has to be in the range 0-100 (fail: price input is blank)| Original error message did not specify this failure. | Changed error message to include this failure. |
||5.5.2| Date must be given in the format YYYYMMDD (fail)| Original function did not validate the expiration date input. | Changed update method to include expiration date validation. |
||5.5.3| Date must be given in the format YYYYMMDD (fail: input includes non-numeric characters)| Original error message did not include this failure. | Changed error message to include this failure. |
||5.5.4| Date must be given in the format YYYYMMDD (fail: input is blank)| Original error message did not include this failure. | Changed error message to include this failure. |
||5.5.5| Date must be given in the format YYYYMMDD (fail: input has separators)| Original error message did not include this failure. | Changed error message to include this failure. |
||5.6.2| Ticket of the given name must exist (fail)| Original error message did not include this failure. | Changed error message to include this failure. |
||5.6.3| Ticket of the given name must exist (fail: only numeric characters))| Original error message did not include this failure. | Changed error message to include this failure. |
||5.6.4| Ticket of the given name must exist (fail: input is blank))| Original error message did not include this failure. | Changed error message to include this failure. |

#####Back End Test Implementation Failures
|Feature Specification|Sub-Section|Sub-Section Description|Problem|Resolution|
|---------------------|-----------|-----------------------|-------|----------|
|TICKET|2.1| A ticket's expiry date should be verified to be not expired. If ticket is not expired the function should return the ticket, if not return None | Test failed because prune_expired_tickets needs a list of tickets to prune. | Added a patch to mock prune_expired_tickets function and mocked a valid_test_tickets list. |
||3.2| The ticket should be added to the database when all input requirements check out, if an error occurs it should be reported (error from .add) | Test failed due to exception not being caught in tickets.py | Added try-catch block in tickets. |
||3.3| The ticket should be added to the database when all input requirements check out, if an error occurs it should be reported (error from .commit) | Test failed due to exception not being caught in tickets.py | Added try-catch block in tickets. |
