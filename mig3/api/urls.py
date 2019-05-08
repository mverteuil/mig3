from django.urls import include, path, re_path

from accounts.api import views as accounts
from builds.api import views as builds
from projects.api import views as projects
from . import views as api

urlpatterns = [
    path("builds/", view=builds.BuildListView.as_view(), name="build_list"),
    path("builds/<str:build_id>/", view=builds.BuildDetailView.as_view(), name="build_detail"),
    path("builders/", view=accounts.BuilderAccountList.as_view(), name="builder_account_list"),
    path("projects/", view=projects.ProjectListView.as_view(), name="project_list"),
    path("projects/<str:project_id>/", view=projects.ProjectTargetListView.as_view(), name="project_detail"),
    path(
        "projects/<str:project_id>/targets/", view=projects.ProjectTargetListView.as_view(), name="project_target_list"
    ),
    path(
        "swagger/",
        include(
            [
                path(route="", view=api.schema_view.with_ui("swagger", cache_timeout=0), name="schema_swagger_ui"),
                re_path(route=r"schema.json", view=api.schema_view.without_ui(cache_timeout=0), name="schema_json"),
            ]
        ),
    ),
    path("targets/<str:target_id>/", view=projects.TargetDetailView.as_view(), name="target_detail"),
    path("targets/<str:target_id>/builds/", view=builds.TargetBuildListView.as_view(), name="target_build_list"),
    path("users/", view=accounts.UserAccountList.as_view(), name="user_account_list"),
]
