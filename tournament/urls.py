from django.urls import path
from .views import tournament_details, tournament_list

urlpatterns = [
    path("<int:tournament_id>/details/", tournament_details, name="tournament_details"),
    path("", tournament_list, name="tournament_list"),
]
