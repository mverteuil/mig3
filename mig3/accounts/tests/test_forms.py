from .. import forms


def test_create_administrator(db):
    """Should create administrator with valid form data."""
    password = "p4ssw0rd!"
    form = forms.CreateAdministratorForm(
        data={"email": "admin@example.com", "name": "Test Administrator", "password1": password, "password2": password}
    )
    assert form.is_valid(), form.errors
    result = form.save()
    assert result.email == "admin@example.com"
    assert result.name == "Test Administrator"
    assert result.check_password(password)


def test_create_administrator_with_weak_password(db):
    """Should require a strong password."""
    password = "password"
    form = forms.CreateAdministratorForm(
        data={"email": "admin@example.com", "name": "Test Administrator", "password1": password, "password2": password}
    )
    assert not form.is_valid()
    assert "This password is too common." in form.errors["password2"]


def test_create_administrator_with_existing(admin_user):
    """Should refuse to create administrator once one already exists."""
    password = "p4ssw0rd!"
    form = forms.CreateAdministratorForm(
        data={"email": "admin@example.com", "name": "Test Administrator", "password1": password, "password2": password}
    )
    assert not form.is_valid()
    assert "Administrator already exists." in form.non_field_errors()
