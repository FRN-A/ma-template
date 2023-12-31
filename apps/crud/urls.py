from django.urls import path

from . import views

app_name = 'crud'

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("create", views.Create.as_view(), name="create"),
    path("edit/<int:pk>", views.Edit.as_view(), name="update"),
    path("delete/<int:pk>", views.Delete.as_view(), name="delete"),
]