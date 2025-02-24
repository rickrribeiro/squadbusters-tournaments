from .views import external_info
from django.urls import path

urlpatterns = [
    path('external_info/', external_info, name='external-info'),
]