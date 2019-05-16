from django.contrib.auth import views as auth_views
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accounts.utils import URLSignature
from . import forms

TEN_MINUTES_IN_SECONDS: int = 60 * 10


class LoginView(auth_views.LoginView):
    """Login user account session."""

    template_name = "login.html"


class LogoutView(auth_views.LogoutView):
    """Logout user account session."""


class CreateAdministratorView(CreateView):
    """Create initial administrator with secret URL."""

    form_class = forms.CreateAdministratorForm
    template_name = "create_administrator.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        """Add form action to view context."""
        context = super().get_context_data(**kwargs)
        context["form_action"] = reverse("create_admin", kwargs={"secret": URLSignature.generate_signature()})
        return context

    def dispatch(self, request, *args, **kwargs):
        """Validate secret signature in the incoming request."""
        if URLSignature.validate_signature(kwargs["secret"], max_age=TEN_MINUTES_IN_SECONDS):
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404
