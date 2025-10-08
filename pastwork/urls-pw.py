from django.urls import path
from . import views

urlpatterns = [
    path("", views.pastwork, name="pastwork"),
    path("<slug:slug>/", views.pastwork_detail, name="pastwork_detail")
]
