from django.urls import path
from . import views
import os

app_name = "Promotion"

urlpatterns = [
    path("", views.homepage, name="Homepage"),
    path("<slug:target_country_slug>/", views.country_page, name="Country"),
    path("<slug:target_country_slug>/<slug:target_brand_slug>/", views.brand_page, name="Brand")
]
