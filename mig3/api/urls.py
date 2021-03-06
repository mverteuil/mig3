from django.urls import path

from accounts.api import views as accounts
from builds.api import views as builds
from projects.api import views as projects
from wizard.api import views as wizard

# fmt: off
urlpatterns = [
    path("builds/", view=builds.BuildListView.as_view(), name="build_list"),
    path("builds/<str:build_id>/", view=builds.BuildDetailView.as_view(), name="build_detail"),
    path("builders/", view=accounts.BuilderAccountListView.as_view(), name="builder_account_list"),
    path("builders/<str:builder_id>/", view=accounts.BuilderAccountDetailView.as_view(), name="builder_account_detail"),
    path("projects/", view=projects.ProjectListView.as_view(), name="project_list"),
    path("projects/<str:project_id>/", view=projects.ProjectDetailView.as_view(), name="project_detail"),
    path("projects/<str:project_id>/targets/", view=projects.ProjectTargetListView.as_view(), name="project_target_list"),
    path("targets/<str:target_id>/", view=projects.TargetDetailView.as_view(), name="target_detail"),
    path("users/", view=accounts.UserAccountListView.as_view(), name="user_account_list"),
    path("users/whoami/", view=accounts.RequestUserAccountDetailView.as_view(), name="request_user_detail"),
    path("wizard/installation-setup/", view=wizard.InstallationSetupDetailView.as_view(), name="installation_setup_detail"),
]
# fmt: on
