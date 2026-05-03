from django.urls import path
from . import views

# Plan URL

urlpatterns = [
    path("", views.get_home, name="get_home")
]
