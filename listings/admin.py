from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published','price','realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'price', 'description', 'address', 'city', 'state', 'zipcode')
    list_per_page = 20

admin.site.register(Listing, ListingAdmin)

# Register your models here.
