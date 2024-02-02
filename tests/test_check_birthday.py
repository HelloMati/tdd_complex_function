from lib.check_birthday import *

def test_check_birthday_old_enough():
    result = check_birthday("1985-02-16")
    assert result == "Access has been granted"

def test_check_birthday_not_old_enough():
    result = check_birthday("2020-02-16")
    assert result == "Access denied"
