from django.urls import path

from builds.api import views as builds

urlpatterns = [path(route="builds/", view=builds.BuildListView.as_view(), name="builds_list")]
