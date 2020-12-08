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