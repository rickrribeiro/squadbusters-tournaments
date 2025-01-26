from django.urls import path
from .views import tournment_details

urlpatterns = [
    path("tournment/<int:tournment_id>/details/", tournment_details, name="tournment_details"),
]
