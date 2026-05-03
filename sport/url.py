from django.urls import path
from . import views

# Sport URL

urlpatterns = [
    path("", views.get_sports, name="get_sports")
]
