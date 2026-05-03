from django.urls import path
from . import views

# Tour URL

urlpatterns = [
    path("", views.get_tours, name="get_tours")
]
