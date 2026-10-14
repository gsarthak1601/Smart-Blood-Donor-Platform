
from blood_request import validate_blood_request


def test_valid_blood_request():
    request = {
        "name": "Rahul",
        "blood_group": "O+",
        "location": "Pune"
    }
    assert validate_blood_request(request) is True


def test_missing_name():
    request = {
        "name": "",
        "blood_group": "O+",
        "location": "Pune"
    }
    assert validate_blood_request(request) is False


def test_invalid_blood_group():
    request = {
        "name": "Rahul",
        "blood_group": "XYZ",
        "location": "Pune"
    }
    assert validate_blood_request(request) is False


def test_missing_location():
    request = {
        "name": "Rahul",
        "blood_group": "O+",
        "location": ""
    }
    assert validate_blood_request(request) is False


def test_request_is_not_a_dictionary():
    assert validate_blood_request(None) is False
