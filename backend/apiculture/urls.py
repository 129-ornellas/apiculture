from django.urls import path

from .views import bees_manager, request_manager

urlpatterns = [
    path("request_manager", request_manager),
    path("bees_manager", bees_manager)
]
