#!/usr/bin/env python
#coding=utf-8

from cdma.apps.station.models import *
from django.contrib import admin
import datetime
    
admin.site.register(Category)

admin.site.register(NewlyStation)
admin.site.register(ExtStation)
admin.site.register(IndoorStation)

admin.site.register(TransInfo)
admin.site.register(TransDetail)
