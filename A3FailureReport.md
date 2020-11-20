# SeetGeek Assignment 3 - Failure Report

`All backend case definitions have been added to testcases/backend`

###Section 1: Aubrey McLeod
I implemented the test set from A1 for features R1 and R8. Additionally I implemented a set of blackbox tests for the backend's validation library (email address validation and password validation).

For the password validator, we had the following criteria: 
- `# passwords must be of length 6 or greater.`
- `# passwords must contain one valid special character.`
- `# passwords must contain one upper case character`
- `# passwords must contain one lower case character`

Basic combinatorics tell us that there are 2^4=16 possible combinations of these criteria, however this is an over count because 
when we have no valid characters, we can have no edge case that also is too short or too long, so we have 1 valid state, and 14 adjacent edge cases.
Additionally, we have the two cases where we have invalid cases (one case being under 6 long, and the other over 6 long). 
So we end up with 17 test cases on this validation, where all fail except for one in which all the above criteria are met.


For the email validator, we wind up with something significantly more complex. The RFC5322 can be summarized by the following criteria:
- `# Emails must have two parts, the local address <= 64 in length, and the domain <= 255`
- `# local address must either be alphanumeric with '.' (not at start or end or next to any other dots) or any of the following '!#$%&'*+-/=?^_{|}~', and have a length greater than 0 but less than 64`
- `# local address may also be encapsulated in double quotes, which allows for any valid printable character, with some exceptions.`
- `# domains must be alpha numeric with options for - (not at the end), with '.' acting as a separator.`
- `# domains may take the form of an ip4 address (contained in '[]') or ipv6, contained in '[]'`

Here then we have two separate classes of local address, and 3 separate classes of domain address.
For the standard form local address we test to see if a base case is accepted, if a double dot is rejected, if a leading dot is rejected, and if a tailing dot is rejected.
For the Quoted address, we test that a base case is accepted and if an invalid quoted case is rejected.
For a standard form domain we test an accepting address, and we test a failing address.
Then we test to see if an IPv4 address is accepted.
Then we test to see if an IPv6 address is accepted.
Next we test the case where there is no at sign, and then we test the case where there are multiple unquoted at signs.
Then we test two cases of invalid character positioning/fomatting in both quoted and standard local addresses.
Finally we test an address with a local part longer than 64 characters.

#####Front End Test Implementation Failures
|Feature Specification|Sub-Section|Sub-Section Description|Problem|Resolution|
|---------------------|-----------|-----------------------|-------|----------|
|R1|1.5| The login form can be submitted as a POST request to the current URL (/login)|Test design was inconsistant with actual webpage functionality: Form POSTed through submit button, followed by page reload and manual POST request.|Applied occam's razor, and only POSTed once through button in actual test.|
| |1.6.2| Email and password both cannot be empty. (check fail)|Test design did not test what was meant to be tested; the fields were populated despite the test requiring empty fields. | Redesigned the test to check that the username and password had the "required" attribute.|
| |1.6.3| Email and password both cannot be empty. | Failed to catch edge case where required tags were manually removed by user; no test called for.| Implemented new test to ensure that an empty POST request to the login route would only trigger the login route to be loaded.|
| |1.7| Email has to follow addr-spec defined in RFC 5322.| Original test design to broad to be an actual test; only specified base -> low coverage. | Original test migrated to 1.7.1, Designed new 1.7.2-4 test cases.|
| |1.7.2| Email has to follow addr-spec defined in RFC 5322. | No case for when email fails to have valid local address in standard form. | Implemented new case test.|
| |1.7.3| Email has to follow addr-spec defined in RFC 5322. | No case for when email has valid local address in quoted form. | Implemented new case test.|
| |1.7.4| Email has to follow addr-spec defined in RFC 5322. | No case for when email fails to have valid local address in quoted form. | Implemented new case test.|
| |1.8| Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character. | Test design specifies normal case behavior but does not test failure case. | moved original design to 1.8.1, and created test 1.8.2 to test failure case.| 
| |1.8.2| Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character. | No case for when password fails to meet standards. | Implemented new test case. |
| |1.9|For any formatting errors, render the login page and show the message “email/password format is incorrect.” | Test design fails to test for invalid data, only uses original valid data to test for formatting error. | Redesigned test so that bad email and password were tested.|
|R8| | | |No errors found in this section. |

#####Backend Test Implementation Failures
|Feature Specification|Sub-Section|Sub-Section Description|Problem|Resolution|
|---------------------|-----------|-----------------------|-------|----------|
|VALIDATION| EMAIL.15 | EMAIL.15- emails must conform to RFC5322, local address is too long(Fail) | Original validator did not test for length > 64 on local address or length >255 on domain, causing the test to pass. | Implemented the required length validation in qa327.library.validation.validate_email_address.

###Section 3: Melissa Zhu
I implemented R3 (from R3.1 to R3.9.1) from the test set in A1.

###Front End Test Implementation Failures
|Feature Specification|Sub-Section|Sub-Section Description|Problem|Resolution|
|---------------------|-----------|-----------------------|-------|----------|
|R3|4| This page shows a logout link, pointing to /logout | There's no id in HTML file to logout link.| Edited index.html to include id="logout" attribute.| 
| |5| This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.| There is no id in HTML file for individual ticket information. | |
| |6| This page contains a form that a user can submit new tickets for sell.| There's no id in HTML file to sell ticket form fields.| Added id attributes to sell ticket form fields: ticket name, quantity, price, expiration and submit.|
| |7| This page contains a form that a user can buy new tickets.| There's no id in HTML file to buy ticket form fields.| Added id attributes to buy ticket fields: ticket name, quantity and submit.|
| |8| This page contains a form that a user can update existing tickets.| There's no id in HTML file to update form fields.| Added id attributes to update ticket fields: ticket name, quantity, price, expiration and submit.|
| |9.1| The ticket-selling form can be posted to /sell. (pass)| #sell-message element does not exist in HTML file| |