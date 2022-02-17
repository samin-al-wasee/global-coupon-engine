from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="Homepage"),
    path("country/", views.country_page, name="Country")
]
