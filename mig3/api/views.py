from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from mig3 import get_version

schema_view = get_schema_view(
    openapi.Info(
        title=f"Mig3 Service ({get_version()})",
        default_version="v1",
        description="Detect regressions in your python3 migration!",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mverteuil@github.com"),
        license=openapi.License(name="GPLv3 License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
