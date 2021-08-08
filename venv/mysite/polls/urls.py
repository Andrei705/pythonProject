from django.urls import path

from . import views



urlpatterns = [

     path(r'object/<int:id>/', views.ObjectListView.as_view()),
     path(r'object/', views.ObjectListView.as_view()),

    ]