from django.contrib import admin
from .views import *
from django.urls import path, include


urlpatterns = [
    path('datetime/', DatetimeView.as_view()),
    path('random/', RandomView.as_view()),
    path('', IndexView.as_view()),
]
