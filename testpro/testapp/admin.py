from django.contrib import admin
from .models import *


class vendor_(admin.ModelAdmin):
    list_display=['company_name']

class Purchhase_(admin.ModelAdmin):
    list_display=['item']

admin.site.register(Vendor,vendor_)
admin.site.register(Purchase,Purchhase_)


# Register your models here.
