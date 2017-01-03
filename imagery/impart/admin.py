from django.contrib import admin

from .models import Contact, LandPrice, Manifesto, NameValuePair, News

admin.site.register(News)
admin.site.register(NameValuePair)
admin.site.register(Manifesto)
admin.site.register(LandPrice)
admin.site.register(Contact)
