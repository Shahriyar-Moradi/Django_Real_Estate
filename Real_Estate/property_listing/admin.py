from django.contrib import admin

from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','price','is_published','list_date','realtor')
    list_display_links=('title',)
    list_filter=('realtor',)
    list_editable=('is_published',)
    search_fields=('city',)
    list_per_page=2
admin.site.register(Listing,ListingAdmin)