import pytest


@pytest.fixture
def valid_form():
    return {
        'email': 'user@mail.com',
        'phone': '+71234567890',
        'age': 25,
        'name': 'Иван Иванов'
    }
    
    