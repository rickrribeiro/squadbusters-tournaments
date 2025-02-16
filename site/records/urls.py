from django.urls import path
from .views import record_list, record_by_clan

urlpatterns = [
    path("", record_list, name="record_list"),
    path("clans", record_by_clan, name="record_by_clan"),
]
