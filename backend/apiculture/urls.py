from django.urls import path

from .views import request_manager, bees_manager

urlpatterns = [
    path("request_manager", request_manager),
    path("bees_manager", bees_manager)
]
