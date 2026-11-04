import pytest

from shop import (
    validate_email,
    validate_phone,
    validate_age,
    validate_name,
    validate_form
)

@pytest.mark.parametrize("email", ["user@mail.com",
])
def test_email_valid(email):
    assert validate_email(email) is True

@pytest.mark.parametrize("email", [
    "user@mailcom",
    "usermail.com",
    "user@@mail.com", 
    "user @mail.com",
    "user@",
])
def test_email_invalid(email):
    with pytest.raises(Exception):
        validate_email(email)
        
@pytest.mark.parametrize("phone", [
    "+71234567890",
    "81234567890",
])
def test_phone_valid(phone):
    assert validate_phone(phone) is True

@pytest.mark.parametrize('phone', [
    "+7123456789",
    "61234567890",
])
def test_phone_invalid(phone):
    with pytest.raises(Exception):
        validate_phone(phone)
        
@pytest.mark.parametrize("age", [14, 25, 120])
def test_age_valid(age):
    assert validate_age(age) is True

@pytest.mark.parametrize("age", [13, 121, -5, "двадцать"])
def test_age_invalid(age):
    with pytest.raises(Exception):
        validate_age(age)
        
@pytest.mark.parametrize("name", [
    "Ан",
    "Иван Иванов",
    "Анна-Мария",
    "А" * 50,
])
def test_name_valid(name):
    assert validate_name(name) is True


@pytest.mark.parametrize("name", [
    "А",
    "А" * 51,
    "Иван123",
    " ",
])
def test_name_invalid(name):
    with pytest.raises(Exception):
        validate_name(name)
        
        
def test_form_valid(valid_form):
    assert validate_form(valid_form) == []


def test_form_invalid_email(valid_form):
    valid_form["email"] = "wrong"
    assert len(validate_form(valid_form)) == 1


def test_form_all_fields_invalid(valid_form):
    valid_form.update({
        "email": "wrong",
        "phone": "123",
        "age": 10,
        "name": "Иван123"
    })

    assert len(validate_form(valid_form)) == 4


def test_form_empty():
    assert len(validate_form({})) == 4
    
    
def test_email_not_string():
    with pytest.raises(Exception):
        validate_email(123)
        
def test_phone_not_string():
    with pytest.raises(Exception):
        validate_phone(123)
        
