"""R1. Проверка электронной почты. Функция validate_email должна принимать адрес, содержащий ровно один символ @, непустые части до и после него, точку в доменной части и не содержащий пробелов.
R2. Проверка номера телефона. Функция validate_phone должна принимать номера в форматах +7XXXXXXXXXX и 8XXXXXXXXXX, содержащие ровно 10 цифр после кода.
R3. Проверка возраста. Функция validate_age должна принимать целые значения от 14 до 120 включительно.
R4. Проверка имени. Функция validate_name должна принимать строки длиной от 2 до 50 символов включительно, содержащие только буквы, пробелы и дефисы.
R5. Проверка всей формы. Функция validate_form(data) должна проверять все 4 поля формы: электронную почту, телефон, возраст и имя.
R6. Сбор ошибок. Функция validate_form(data) должна возвращать список, содержащий все обнаруженные ошибки, а не только первую.
R7. Успешная проверка. Если все 4 поля заполнены корректно, функция validate_form(data) должна возвращать пустой список ошибок.
R8. Обработка некорректных данных. Если хотя бы одно из 4 полей содержит некорректное значение, функция validate_form(data) должна возвращать непустой список ошибок.
"""


def validate_email(email):
    """Проверяет корректность электронной почты."""
    if not isinstance(email, str):
        raise Exception('Адрес электронной почты должен быть строкой.')
    if email.count('@') != 1:
        raise Exception('Адрес электронной почты должен содержать ровно одну собачку.')
    local_part, domain_part = email.split('@')
    if not local_part or not domain_part:
        raise Exception('Часть адреса почты пустует.')
    if any(c.isspace() for c in email):
        raise Exception('Адрес электронной почты не должен содержать пробелов.')
    if '.' not in domain_part:
        raise Exception('Некорректный домен электронной почты.')
    return True


def validate_phone(phone):
    """Проверяет корректность номера телефона."""
    if not isinstance(phone, str):
        raise Exception('Номер телефона должен быть строкой.')
    if phone.startswith('+7') and len(phone) == 12 and phone[2:].isdigit():
        return True
    if phone.startswith('8') and len(phone) == 11 and phone[1:].isdigit():
        return True
    raise Exception('Некорректный номер телефона.')

def validate_age(age):
    """Проверяет корректность возраста."""
    if type(age) is int and 15 <= age < 120:
        return True
    raise Exception('Некорректный возраст.')


def validate_name(name):
    """Проверяет корректность имени."""
    if (
        isinstance(name, str)
        and 2 <= len(name) < 50
        and any(c.isalpha() for c in name)
        #and all(c.isalpha() or c in ' -' for c in name)
    ):
        return True
    raise Exception('Некорректное имя.')


def validate_form(data):
    """Проверяет корректность всех полей формы и возвращает список ошибок."""
    errors = []
    validators = [
        ('email', validate_email, 'Некорректный адрес электронной почты.'),
        ('phone', validate_phone, 'Некорректный номер телефона.'),
        ('age', validate_age, 'Некорректный возраст.'),
        ('name', validate_name, 'Некорректное имя.')
    ]
    for field, validator, message in validators:
        try:
            validator(data.get(field, ''))
        except Exception:
            errors.append(message)
    return errors

