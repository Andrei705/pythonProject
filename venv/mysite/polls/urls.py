from django.urls import path

from . import views



urlpatterns = [
    path('object/', views.ObjectListView.as_view())
    ]