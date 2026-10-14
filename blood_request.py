
VALID_BLOOD_GROUPS = [
    "A+", "A-", "B+", "B-",
    "AB+", "AB-", "O+", "O-"
]


def validate_blood_request(request):
    """Validate basic fields in a demo blood request."""

    if not isinstance(request, dict):
        return False

    name = request.get("name", "")
    blood_group = request.get("blood_group", "")
    location = request.get("location", "")

    if not isinstance(name, str) or not name.strip():
        return False

    if blood_group not in VALID_BLOOD_GROUPS:
        return False

    if not isinstance(location, str) or not location.strip():
        return False

    return True
