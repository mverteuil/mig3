from django.urls import include, path, re_path

from accounts.api import views as accounts
from builds.api import views as builds
from projects.api import views as projects
from wizard.api import views as wizard
from . import views as api

schema_patterns = [
    path(route="", view=api.schema_view.with_ui("swagger", cache_timeout=0), name="schema_swagger_ui"),
    re_path(route=r"schema.json", view=api.schema_view.without_ui(cache_timeout=0), name="schema_json"),
]

urlpatterns = [
    path("builds/", view=builds.BuildListView.as_view(), name="build_list"),
    path("builds/<str:build_id>/", view=builds.BuildDetailView.as_view(), name="build_detail"),
    path("builders/", view=accounts.BuilderAccountList.as_view(), name="builder_account_list"),
    path("installation-setup/", view=wizard.InstallationSetupDetailView.as_view(), name="installation_setup_detail"),
    path("projects/", view=projects.ProjectListView.as_view(), name="project_list"),
    path("projects/<str:project_id>/", view=projects.ProjectDetailView.as_view(), name="project_detail"),
    path("swagger/", include(schema_patterns)),
    path("targets/<str:target_id>/", view=projects.TargetDetailView.as_view(), name="target_detail"),
    path("users/", view=accounts.UserAccountList.as_view(), name="user_account_list"),
    path("whoami/", view=accounts.RequestUserAccountDetail.as_view(), name="request_user_detail"),
]
