#coding=utf-8
from django.contrib import databrowse
from apps.project.models import *
from apps.deptment.models import *
from apps.car.models import *

databrowse.site.register(DailyWork)
databrowse.site.register(Deptment)

