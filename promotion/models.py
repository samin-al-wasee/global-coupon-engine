from datetime import datetime
from django.utils.text import slugify
from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


def rename_country_logos(instance, filename):
	filebase, extension = filename.split('.')
	if instance.pk:
		return "images/country_flags/{}.{}".format(slugify(instance.pk), extension)
	else:
		return "images/country_flags/{}.{}".format(instance.country_slug, extension)


def rename_brand_logo(instance, filename):
	filebase, extension = filename.split('.')
	if instance.pk:
		return "images/brand_logos/{}.{}".format(slugify(instance.pk), extension)
	else:
		return "images/brand_logos/{}.{}".format(instance.brand_slug, extension)


class Country(models.Model):
	country_name = models.CharField(max_length=50, unique=True, verbose_name="Name")
	country_slug = models.SlugField(editable=False)
	country_logo = models.FileField(upload_to=rename_country_logos, verbose_name="Logo")
	
	class Meta:
		verbose_name = 'Country'
		verbose_name_plural = 'Countries'
		ordering = ['country_name']
		
	def save(self, *args, **kwargs):
		self.country_slug = slugify(self.country_name)
		super(Country, self).save(*args, **kwargs)
		
	def get_absolute_url(self):
		return reverse("Promotion:Country", args=[self.country_slug])
		
	def __str__(self):
		return self.country_name


class Brand(models.Model):
	exists_in = models.ManyToManyField(Country, verbose_name='Countries')
	brand_name = models.CharField(max_length=50, unique=True, verbose_name="Name")
	brand_slug = models.SlugField(editable=False)
	brand_logo = models.FileField(upload_to=rename_brand_logo, verbose_name="Logo")
	brand_link = models.CharField(max_length=200, verbose_name="URL")
	
	class Meta:
		ordering = ['brand_name']
		
	def save(self, *args, **kwargs):
		self.brand_slug = slugify(self.brand_name)
		super(Brand, self).save(*args, **kwargs)
	
	def __str__(self):
		return self.brand_name


class Offer(models.Model):
	choices_offer_type = [
		("CODE", "Code"),
		("DEAL", "Deal"),
	]
	validators_offer_amount = [
		MinValueValidator(0),
		MaxValueValidator(100),
	]
	offer_title = models.CharField(max_length=50, verbose_name="Title")
	offer_details = models.TextField(max_length=300, verbose_name='Description')
	offered_by = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Brand')
	offered_in = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country')
	offer_type = models.CharField(max_length=4, choices=choices_offer_type, verbose_name="Type")
	offer_amount = models.IntegerField(validators=validators_offer_amount, verbose_name='Amount')
	offer_code = models.CharField(max_length=30, verbose_name="Code", help_text="Leave this field empty for deals.", default="You don't need any code!")
	offer_expires_on = models.DateField(verbose_name='Expires On')
	offer_next_available_on = models.DateField(verbose_name='Next Available On')
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
	username = models.CharField(max_length=50, verbose_name="Username")
	comment = models.TextField(max_length=1000, verbose_name='Comment')
	comment_created_on = models.DateTimeField(auto_now_add=True)
	comment_last_updated_on = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ['-comment_last_updated_on', '-comment_created_on']
		
	def __str__(self):
		return str(self.username) + ", " + str(self.comment_created_on)
		