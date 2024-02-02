from datetime import datetime

def check_birthday(birth_date):
    birth_date_obj = datetime.strptime(birth_date, '%Y-%m-%d').date()

    current_date = datetime.now().date()

    age = current_date.year - birth_date_obj.year - ((current_date.month, current_date.day) < (birth_date_obj.month, birth_date_obj.day))

    if age >= 16:
        return "Access has been granted"
    return "Access denied"
