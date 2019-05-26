from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from accounts import views as accounts


class BridgeView(accounts.AdministratorRequiredMixin, LoginRequiredMixin, TemplateView):
    """Bridge view between Vue and Django."""

    template_name = "index.html"
