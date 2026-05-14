from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display =('id','title','is_published', 'list_data', "doctor")
    list_display_links =('id', 'title')
    list_filter = ('doctor', )
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address',)
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)