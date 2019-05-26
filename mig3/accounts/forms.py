from datetime import timedelta

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from accounts.utils import URLSignature


class CreateAdministratorForm(UserCreationForm):
    """Create administrator accounts."""

    class Meta:  # noqa: D106
        model = get_user_model()
        fields = ("email", "name", "password1", "password2")

    def clean(self):
        """Ensure that administrator hasn't already been created."""
        if get_user_model().objects.filter(is_superuser=True).exists():
            raise ValidationError("Administrator already exists.")
        return super().clean()

    def save(self, commit: bool = True):
        """Create superuser with validated form data."""
        return self._meta.model.objects.create_superuser(
            **{
                "email": self.cleaned_data["email"],
                "name": self.cleaned_data["name"],
                "password": self.cleaned_data["password1"],
                "commit": commit,
            }
        )


class SecretCodeForm(forms.Form):
    """Validate secret code to bootstrap installation with initial administrator."""

    secret_code = forms.CharField(max_length=128)

    def clean_secret_code(self):
        """Check for invalidation by time or value."""
        secret_code = self.cleaned_data["secret_code"]
        URLSignature.validate_signature(secret_code, max_age=timedelta(minutes=10))
        return secret_code
