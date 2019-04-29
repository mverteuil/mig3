from django.urls import path, re_path

from builds.api import views as builds

from . import views as api

urlpatterns = [
    path(route="builds/", view=builds.BuildListView.as_view(), name="builds_list"),
    re_path(
        route=r"swagger(?P<format>\.json|\.yaml)", view=api.schema_view.without_ui(cache_timeout=0), name="schema_json"
    ),
    path(route="swagger/", view=api.schema_view.with_ui("swagger", cache_timeout=0), name="schema_swagger_ui"),
    path(route="redoc/", view=api.schema_view.with_ui("redoc", cache_timeout=0), name="schema_redoc"),
]
