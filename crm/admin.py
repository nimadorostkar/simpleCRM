from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from django.contrib.admin.models import LogEntry
from . import models
from .models import Product


#------------------------------------------------------------------------------
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('name','cost', 'j_date_created', 'image_tag')
    search_fields = ['name']

admin.site.register(models.Product, ProductAdmin)



#------------------------------------------------------------------------------
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('name','phone', 'address')
    search_fields = ['name']

admin.site.register(models.Customer, CustomerAdmin)



admin.site.register(Order)
