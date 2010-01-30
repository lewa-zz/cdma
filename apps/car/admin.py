#coding=utf-8
from apps.car.models import *
from django.contrib import admin
import datetime

class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('基本资料',{'fields': ['carnumber','driver','phone','type','islend']}),
        ('成本项', {'fields': ['cost'], 'classes': ['wide', 'extrapretty'],}),
    ]
    list_filter = ['islend']
    search_fields = ['carnumber']

admin.site.register(Car, CarAdmin)

class CarDailyAdmin(admin.ModelAdmin):
    list_display = ['car','workingdate','deptment','place']
    list_filter = ['deptment']
    search_fields = ['place']

admin.site.register(CarDaily, CarDailyAdmin)
