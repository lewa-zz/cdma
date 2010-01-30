#coding=utf-8
from apps.project.models import *
from django.contrib import admin
import datetime

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name','wbs','designnumber','innernumber','deptment','projectstate']}),
        ('预算自购材料金额', {'fields': ['budget'], 'classes': ['collapse']}),
    ]

#    list_display = ('question','pub_date','was_published_today')
    list_filter = ['deptment']
    search_fields = ['name']

admin.site.register(Project, ProjectAdmin)
