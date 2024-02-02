## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

 Birthday_record_keeping(date_of_birth):

def check_birthday(name, birthday):
    """Check if the user is old enough(16 years old) and grant access or deny

    """
    pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a string format date of birth the function determins if the user is old enough to grant access.
"""
extract_uppercase("2001-01-16") => "Access has been granted"
extract_uppercase("2016-01-16") => "Access denied"


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

```python

from lib. import *

"""
Given birthday it will return "Access has been granted"
"""
def test_check_birthday_old_enough():
    result = check_birthday("2001-02-16")
    assert result == "Access has been granted"

def test_check_birthday_not_old_enough():
    result = check_birthday("2020-02-16")
    assert result == "Access denied"

```
