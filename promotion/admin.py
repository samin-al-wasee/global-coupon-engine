from django.contrib import admin
from promotion.models import Country, Brand, Offer, Comment

admin.site.site_header = "Global Coupon Engine"

admin.site.register(Country)
admin.site.register(Brand)
admin.site.register(Offer)
admin.site.register(Comment)