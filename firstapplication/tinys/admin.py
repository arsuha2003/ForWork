from django.contrib import admin
from .models import Tiny

admin.site.register(Tiny)

# class TinyAdmin(admin.ModelAdmin):
#     list_display = ('full_url', 'short_url')
