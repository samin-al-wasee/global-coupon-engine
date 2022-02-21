from django.shortcuts import render
from promotion.models import Country, Brand, Offer, Comment
from datetime import date

def homepage(request):
	countries = Country.objects.all()
	context = {"countries": countries}
	render(request, "country_list_footer.html", context)
	return render(request, "homepage.html", context)


def country_page(request, target_country_slug):
	target_country = Country.objects.get(country_slug=target_country_slug)
	brands = Brand.objects.filter(exists_in=target_country)
	offers = Offer.objects.filter(offered_in=target_country)
	context = {"target_country": target_country, "brands": brands, "offers": offers}
	return render(request, "country_page.html", context)


def brand_page(request, target_country_slug, target_brand_slug):
	target_country = Country.objects.get(country_slug=target_country_slug)
	target_country_brands = Brand.objects.filter(exists_in=target_country)
	target_brand = Brand.objects.get(brand_slug=target_brand_slug)
	available_offers = Offer.objects.filter(offer_expires_on__gte=date.today(), offered_by=target_brand, offered_in=target_country)
	expired_offers = Offer.objects.filter(offer_expires_on__lte=date.today())
	comments = Comment.objects.all()
	current_month_year = date.today().strftime("%B") + ", " + date.today().strftime("%Y")
	context = {"target_country": target_country, "target_country_brands": target_country_brands, "target_brand": target_brand, "available_offers": available_offers, "expired_offers": expired_offers, "comments": comments, "current_month_year": current_month_year}
	return render(request, "brand_page.html", context)
