from django.contrib import admin

from .models import Contact, LandPrice, ManifestoTheme, NameValuePair, News

admin.site.register(News)
admin.site.register(NameValuePair)
admin.site.register(ManifestoTheme)
admin.site.register(LandPrice)
admin.site.register(Contact)
