from django.shortcuts import render
from promotion.models import Country


def homepage(request):
	countries = Country.objects.all()
	context = {"countries": countries}
	render(request, "country_list_footer.html", context)
	return render(request, "homepage.html", context)
