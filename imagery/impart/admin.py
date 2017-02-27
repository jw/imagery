from .models import Contact, LandPrice, Manifest, Content, News, Artist, Art, Tag

from django.contrib import admin

admin.site.register(News)
admin.site.register(Content)
admin.site.register(Manifest)
admin.site.register(LandPrice)
admin.site.register(Contact)
admin.site.register(Artist)
admin.site.register(Art)
admin.site.register(Tag)
