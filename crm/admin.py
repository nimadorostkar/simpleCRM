from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from django.contrib.admin.models import LogEntry
from . import models
from .models import Product
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin




#------------------------------------------------------------------------------
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('name','cost', 'image_tag')
    search_fields = ['name']

admin.site.register(models.Product, ProductAdmin)



#------------------------------------------------------------------------------
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('name','phone', 'address')
    search_fields = ['name']

admin.site.register(models.Customer, CustomerAdmin)



#------------------------------------------------------------------------------
class OrderAdmin(ModelAdminJalaliMixin,ImportExportModelAdmin):
    list_display = ('customer','product', 'status')

admin.site.register(models.Order, OrderAdmin)






#
