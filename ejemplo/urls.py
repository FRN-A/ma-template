from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name=""),
    path("indexitem", views.indexitem, name=""),
    path("create", views.create, name=""),
]