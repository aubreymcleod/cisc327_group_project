# SeetGeek Assignment 5 - Design Report  

###Section 1: Aubrey McLeod
  
#####<u>Integration Tests</u>  
There are two tests, one where a user signs in and lists a ticket for sale(test 1), and another test where a user logs on and buys a ticket (test 2).
The tests are depicted below.
```
#Test 1 Protocol:
- the user opens up the registration route
- the user enters their email (test0@test.sb.com) into the email field.
- the user enters their name (test0) into the name field
- the user enters their password (Test0!) into the password field.
- the user reenters their password (Test0!) into the password confirmation field.
- the user clicks "submit"

- the user opens the login route
- the user enters their email (test0@test.sb.com) into the email field.
- the user enters their password (Test0!) into the password field.
- the user clicks "submit"

- the user opens the home route
- the user enters "Test Ticket" into the #sell-ticket-name field.
- the user enters "10" into the #sell-quantity field.
- the user enters "100" into the #sell-price field.
- the user enters "20211231" into the #sell-expiration field.
- the user clicks "#sell-submit"

- the user validates that a new entry exists in the ticket listings
- the user validates that the new entry has "(x10)" listed as its quantity.
- the user validates that the new entry has the name "Test Ticket" listed as its name.
- the user validates that the new entry has the price "$100" listed as its price.
- the user clicks "#logout"
- the user disconnects.
```

```
#Test 2 Protocol:
- the user opens up the registration route
- the user enters their email (test1@test.sb.com) into the email field.
- the user enters their name (test1) into the name field
- the user enters their password (Test1!) into the password field.
- the user reenters their password (Test1!) into the password confirmation field.
- the user clicks "submit"

- the user opens the login route
- the user enters their email (test1@test.sb.com) into the email field.
- the user enters their password (Test1!) into the password field.
- the user clicks "submit"

- the user opens the home route
- the user validates that the #user-balance element says "Your balance is 5000"
- the user enters "Test Ticket" into the "#buy-ticket-name" field.
- the user enters "10" into the "#buy-quantity" field.
- the user clicks "#buy-submit"

- the user validates that the #user-balance element says "Your balance is 3600"
- the user clicks "#logout"
- the user disconnects.
```


  
#####<u>Whitebox Tests</u>
Here we will test `validation.validate_name()`:
```
def validate_name(name):
    if re.match("^[a-zA-Z0-9][a-zA-Z0-9 ]*[a-zA-Z0-9]$", name) and 6 <= len(name) <= 60:
        return True                 # branch - 1: outcome True
    return False                    # branch - 2: outcome False
```
| Test case | Match Regex | 6<=len(name)<=60 | Branch | Outcome | Test Value |
|-----------|-------------|------------------|--------|---------|------------|
| 1 | False | False | 2 | False | "@" |
| 2 | False | True  | 2 | False | "@@@@@@" |
| 3 | True | False | 2 | False | "a" |
| 4 | True | True | 1 | True | "aaaaaa" |


Here we will test `validation.validate_date()`:
```
def validate_date(expiration_date):
    todays_date = date.today().strftime("%Y/%m/%d")
    if re.match("^[0-9][0-9][0-9][0-9](0[1-9]|1[0-2])([0][1-9]|[1-2][0-9]|3[0-1])$",
                expiration_date) and expiration_date >= todays_date:
        return True                     # branch - 1: outcome True
    return False                        # branch - 2: outcome False
```

| Test case | Match Regex | Date>Today | Branch | Outcome | Test Value |
|-----------|-------------|------------|--------|---------|------------|
| 1 | False | False | 2 | False | "00000000" |
| 2 | False | True  | 2 | False | "20213112" |
| 3 | True | False | 2 | False | "19700101" |
| 4 | True | True | 1 | True | "20201231" |

Here we will test `validation.validate_quantity()`:
```
def validate_quantity(qty):
    try:
        if 0 < int(qty) <= 100:
            return True                 # branch - 1: outcome True
    except:
        return False                    # branch - 2: outcome False
    return False                        # branch - 3: outcome False
```
| Test case | Valid Int | 0<qty<=100 | Branch | Outcome | Test Value |
|-----------|-----------|------------|--------|---------|------------|
| 1 | False | False | 2 | False | "zero" |
| 2 | False | True  | 2 | False | "1E" |
| 3 | True | False | 3 | False | "0" |
| 4 | True | True | 1 | True | "1" |

Here we will test `validation.validate_price()`:
```
def validate_price(price):
    try:
        if 10 <= int(price) <= 100:
            return True                 # branch - 1: outcome True
    except:
        return False                    # branch - 2: outcome False
    return False                        # branch - 3: outcome False

```

| Test case | Valid Int | 0<price<=100 | Branch | Outcome | Test Value |
|-----------|-----------|--------------|--------|---------|------------|
| 1 | False | False | 2 | False | "MILLION" |
| 2 | False | True  | 2 | False | "1E" |
| 3 | True | False | 3 | False | "9" |
| 4 | True | True | 1 | True | "10" |