from django.urls import path, re_path

from . import views



urlpatterns = [
    re_path(r'^object/id=0|$', views.ObjectListView.as_view())
    ]