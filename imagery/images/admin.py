from django.contrib import admin

from .models import Tag, Artist, Art

admin.site.register(Artist)
admin.site.register(Art)
admin.site.register(Tag)
