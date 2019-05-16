from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CreateAdministratorForm(UserCreationForm):
    """Create administrator accounts."""

    class Meta:  # noqa: D106
        model = get_user_model()
        fields = ("email", "name", "password1", "password2")

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
