from django.urls import path

from . import views

urlpatterns = [
    path("to-do/create/", views.ToDoView.as_view()),
    path("to-do/", views.ToDoListView.as_view()),
    path("to-do/<str:to_do_id>/completed/", views.ToDoCompleteView.as_view()),
]
