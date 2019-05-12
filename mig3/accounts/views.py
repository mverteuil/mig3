from django.contrib.auth import views as auth_views


class LoginView(auth_views.LoginView):
    """Login user account session."""

    template_name = "login.html"


class LogoutView(auth_views.LogoutView):
    """Logout user account session."""
