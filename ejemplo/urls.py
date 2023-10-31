from django.urls import path

from . import views

app_name = 'ejemplo'

urlpatterns = [
    path("", views.index, name="index"),
    path("indexitem", views.indexitem, name="indexitem"),
    path("create", views.Create.as_view(), name="create"),
    path("create-loading", views.CreateLoading.as_view(), name="create-loading"),
    path("create-sweatalert", views.CreateSweatalert.as_view(), name="create-sweatalert"),
]