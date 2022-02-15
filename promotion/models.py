from django.db import models

class Country(models.Model):
	country_name = models.CharField(max_length=20, primary_key=True, verbose_name="Country Name")
	country_flag = models.ImageField(upload_to="country_flags/", unique=True, verbose_name="Country Flag")
	
class Brand(models.Model):
	brand_name = models.CharField(max_length=20, primary_key=True, verbose_name="Brand Name")
	brand_logo = models.ImageField(upload_to="brand_logos/", unique=True, verbose_name="Brand Name")
