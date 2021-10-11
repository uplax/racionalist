from django.contrib import admin

from offers.models import OfferPoint, Offer


class OfferPointAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OfferPoint._meta.get_fields() if field.name != 'offer']


admin.site.register(OfferPoint, OfferPointAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Offer._meta.get_fields()]


admin.site.register(Offer, OfferAdmin)
