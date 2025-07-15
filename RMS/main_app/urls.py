from django.urls import path
from .views import Recruiterview
urlpatterns = [
    path('recruiter/',Recruiterview)
]
