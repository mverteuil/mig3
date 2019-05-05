from django.urls import include, path, re_path

from builds.api import views as builds
from projects.api import views as projects
from . import views as api

urlpatterns = [
    path("builds/", view=builds.BuildListView.as_view(), name="build_list"),
    path("builds/<str:pk>/", view=builds.BuildDetailView.as_view(), name="build_detail"),
    path("projects/", view=projects.ProjectListView.as_view(), name="project_list"),
    path(
        "swagger/",
        include(
            [
                path(route="", view=api.schema_view.with_ui("swagger", cache_timeout=0), name="schema_swagger_ui"),
                re_path(route=r"schema.json", view=api.schema_view.without_ui(cache_timeout=0), name="schema_json"),
            ]
        ),
    ),
    path("targets/<str:pk>/", view=projects.TargetDetailView.as_view(), name="target_detail"),
]
