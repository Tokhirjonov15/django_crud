from django.urls import path
from . import views

# Plan URL

urlpatterns = [
    path("", views.get_home, name="get_home"),
    path("plans/create/", views.create_plan, name="create_plan"),
    path("plans/<int:pk>/update/", views.update_plan, name="update_plan"),
    path("plans/<int:pk>/delete/", views.delete_plan, name="delete_plan"),
]
