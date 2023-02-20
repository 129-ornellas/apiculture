from django.urls import path

from . import views

urlpatterns = [
    path("get", views.get),
    path("post", views.post),
    path("put", views.put),
    path("patch", views.patch),
    path("delete", views.delete),
]
