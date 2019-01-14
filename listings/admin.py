from django.contrib import admin

# Register your models here.
from .models import Listing

class ListingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state','zipcode','price')
    list_per_page = 2

admin.site.register(Listing,ListingsAdmin)
