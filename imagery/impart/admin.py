from django.contrib import admin

from .models import Contact, LandPrice, Manifest, NameValuePair, News, Artist, Art, Tag

from django.contrib import admin

from markdownx.admin import MarkdownxModelAdmin

admin.site.register(News, MarkdownxModelAdmin)

# admin.site.register(News)

admin.site.register(NameValuePair)
admin.site.register(Manifest)
admin.site.register(LandPrice)
admin.site.register(Contact)
admin.site.register(Artist)
admin.site.register(Art)
admin.site.register(Tag)
