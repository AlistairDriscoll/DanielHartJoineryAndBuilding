from django.urls import path
from . import views

urlpatterns = [
    path("", views.enquiry_page, name="enquiry_page"),
    path("success/", views.enquiry_success, name="enquiry_success"),
    path("failure/", views.enquiry_failure, name="enquiry_failure"),
]
