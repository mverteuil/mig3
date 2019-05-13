from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class BridgeView(LoginRequiredMixin, TemplateView):
    """Bridge view between Vue and Django."""

    template_name = "index.html"
