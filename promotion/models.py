from django.db import models
from datetime import datetime
from uuid import uuid4


def rename_country_logos(instance, filename):
	filebase, extension = filename.split('.')
	if instance.pk:
		return "images/country_logos/{}.{}".format(instance.pk, extension)
	else:
		return "images/country_logos/{}.{}".format(instance.country_name, extension)


def rename_brand_logo(instance, filename):
	filebase, extension = filename.split('.')
	if instance.pk:
		return "images/brand_logos/{}.{}".format(instance.pk, extension)
	else:
		return "images/brand_logos/{}.{}".format(uuid4().hex(), extension)


class Country(models.Model):
	country_name = models.CharField(max_length=20, unique=True, verbose_name="Country Name")
	country_logo = models.ImageField(upload_to=rename_country_logos, verbose_name="Country Logo")
	
	class Meta:
		verbose_name = 'Country'
		verbose_name_plural = 'Countries'
		ordering = ['country_name']
	
	def __str__(self):
		return self.country_name


class Brand(models.Model):
	exists_in = models.ManyToManyField(Country, verbose_name='Countries')
	brand_name = models.CharField(max_length=100, unique=True, verbose_name="Brand Name")
	brand_logo = models.ImageField(upload_to=rename_brand_logo, verbose_name="Brand Logo")
	brand_link = models.CharField(max_length=200, verbose_name="Brand URL")
	
	class Meta:
		ordering = ['brand_name']
	
	def __str__(self):
		return self.brand_name


class Offer(models.Model):
	offer_title = models.CharField(max_length=256, verbose_name="Offer Title")
	offered_by = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Brand')
	offer_type = models.CharField(max_length=20, verbose_name='Offer Type')
	offered_in = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country')
	offer_details = models.TextField(max_length=1000, verbose_name='Description')
	offer_amount = models.FloatField(verbose_name='Amount')
	offer_expires_on = models.DateTimeField(verbose_name='Expires On')
	offer_next_available_on = models.DateTimeField(verbose_name='Next Available On')
	offer_created_on = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
	offer_last_updated_on = models.DateTimeField(auto_now=True, verbose_name='Last Updated On')
	
	class Meta:
		ordering = ['-offer_last_updated_on', '-offer_created_on']
	
	def is_expired(self):
		if datetime.today() > self.offer_expires_on:
			return True
		return False
	
	def __str__(self):
		return self.offer_title


class Comment(models.Model):
	username = models.CharField(max_length=256, verbose_name="Username")
	comment = models.TextField(max_length=1000, verbose_name='Comment')
	comment_created_on = models.DateTimeField(auto_now_add=True)
	comment_last_updated_on = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ['-comment_last_updated_on', '-comment_created_on']
		