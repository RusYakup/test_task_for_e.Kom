import pytest
from data_validation_utils.field_validation import get_field_type


@pytest.fixture
def test_data():
    return [
        ("2022.01.01", "date"),
        ("01.01.2022", "date"),
        ("7 123 456 78 90", "phone"),
        ("test@example.com", "email"),
        ("Hello, World!", "text"),
        ("", "text"),
        ("2022-01-01", "text"),
        ("+7 1234567890", "text"),
        ("test@example", "text")
    ]


def test_get_field_type(test_data):
    for value, expected_type in test_data:
        result = get_field_type(value)
        print(f"Value: {value}, Expected Type: {expected_type}, Actual Type: {result}")
        assert get_field_type(value) == expected_type
