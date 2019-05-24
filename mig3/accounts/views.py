from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from accounts.utils import URLSignature
from wizard.models import HasAdministrator
from . import forms


class AdministratorRequiredMixin:
    """Require Administrator UserAccount to exist, redirect to the secret code view until one exists."""

    secret_code_url = reverse_lazy("secret_code")

    def dispatch(self, request, *args, **kwargs) -> HttpResponse:
        """Redirect request if administrator does not exist, or pass."""
        if not HasAdministrator.check():
            return HttpResponseRedirect(redirect_to=self.secret_code_url)
        return super().dispatch(request, *args, **kwargs)


class CreateAdministratorView(generic.CreateView):
    """Create initial administrator with secret URL."""

    form_class = forms.CreateAdministratorForm
    template_name = "create_administrator.html"
    success_url = reverse_lazy("bridge")

    def get_context_data(self, **kwargs) -> dict:
        """Add form action to view context."""
        context = super().get_context_data(**kwargs)
        context["form_action"] = reverse("create_admin", kwargs={"secret_code": URLSignature.generate_signature()})
        return context

    def form_valid(self, form):
        """Create login session for the administrator."""
        response = super().form_valid(form)
        administrator = auth.authenticate(
            request=self.request, username=form.data["email"], password=form.data["password1"]
        )
        # Usually, we now check login is allowed. This user is being created in this request, so it's safe to assume they're active.
        auth.login(self.request, administrator)
        return response

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """Validate secret signature in the incoming request."""
        if forms.SecretCodeForm(data={"secret_code": kwargs["secret_code"]}).is_valid():
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(redirect_to=reverse("secret_code"))


class LoginView(AdministratorRequiredMixin, auth_views.LoginView):
    """Login user account session."""

    template_name = "login.html"


class LogoutView(auth_views.LogoutView):
    """Logout user account session."""


class SecretCodeView(generic.FormView):
    """Redirect request using secret code."""

    form_class = forms.SecretCodeForm
    template_name = "secret_code.html"

    def form_valid(self, form: forms.SecretCodeForm) -> HttpResponseRedirect:
        """Redirect to CreateAdministratorView."""
        return HttpResponseRedirect(
            redirect_to=reverse("create_admin", kwargs={"secret_code": form.cleaned_data["secret_code"]})
        )
