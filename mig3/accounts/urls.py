from django.urls import path, re_path

from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("secret-code/", views.SecretCodeView.as_view(), name="secret_code"),
    re_path(r"^create-admin-(?P<secret_code>.*)/$", views.CreateAdministratorView.as_view(), name="create_admin"),
]
