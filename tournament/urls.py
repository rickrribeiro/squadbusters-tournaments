from django.urls import path
from .views import tournament_details, tournament_list

urlpatterns = [
    path("tournament/<int:tournament_id>/details/", tournament_details, name="tournament_details"),
    path("tournaments", tournament_list, name="tournament_list"),
]
