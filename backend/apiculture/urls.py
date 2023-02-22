from django.urls import path

from .views import request_manager

urlpatterns = [
    path("request_manager", request_manager),
]
