from django.shortcuts import render
from promotion.models import Country, Brand, Offer


def homepage(request):
	countries = Country.objects.all()
	context = {"countries": countries}
	render(request, "country_list_footer.html", context)
	return render(request, "homepage.html", context)

def country_page(request):
	brands = Brand.objects.all()
	offers = Offer.objects.all()
	context = {"brands": brands, "offers": offers}
	return render(request, "country_page.html", context)
	
