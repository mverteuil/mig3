from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserAccount = get_user_model()

DEFAULT_PARAMETERS = {"email": "user@example.com", "name": "Test User", "password": "TestPassword", "is_active": True}


def test_create_user(db):
    """Should create UserAccount with default parameters."""
    user = UserAccount.objects.create_user(**DEFAULT_PARAMETERS)

    # Password is now hashed, so cannot be tested normally
    parameters = DEFAULT_PARAMETERS.copy()
    password = parameters.pop("password")

    assert user.check_password(password)

    for key, value in parameters.items():
        assert getattr(user, key) == value, getattr(user, key)


def test_create_superuser(db):
    """Should create UserAccount with superuser privileges with default parameters."""
    user = UserAccount.objects.create_superuser(**DEFAULT_PARAMETERS)

    # Password is now hashed, so cannot be tested normally
    parameters = DEFAULT_PARAMETERS.copy()
    parameters["is_staff"] = True
    parameters["is_superuser"] = True
    password = parameters.pop("password")

    assert user.check_password(password)

    for key, value in parameters.items():
        assert getattr(user, key) == value, getattr(user, key)


def test_create_active_user(db):
    """Should authenticate users in active state."""
    user = UserAccount.objects.create_user(**DEFAULT_PARAMETERS)
    parameters = DEFAULT_PARAMETERS.copy()
    password = parameters.pop("password")
    assert ModelBackend().authenticate(None, username=user.email, password=password)


def test_create_inactive_user(db):
    """Should be not authenticate users in inactive state."""
    parameters = DEFAULT_PARAMETERS.copy()
    parameters["is_active"] = False

    user = UserAccount.objects.create_user(**parameters)
    password = parameters.pop("password")
    assert not ModelBackend().authenticate(None, username=user.email, password=password)
