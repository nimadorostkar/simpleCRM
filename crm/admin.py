from django.contrib import admin
from .models import *





#------------------------------------------------------------------------------
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('name','cost', 'j_date_created', 'image_tag')
    search_fields = ['name']

admin.site.register(models.Product, ProductAdmin)



admin.site.register(Customer)
admin.site.register(Order)
