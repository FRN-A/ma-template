from django.urls import path

from . import views

app_name = 'ejemplo'

urlpatterns = [
    path("", views.index, name="index"),
    path("indexitem", views.indexitem, name=""),
    path("create", views.Create.as_view(), name=""),
]