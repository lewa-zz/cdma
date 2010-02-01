#coding=utf-8




from apps.dailywork.models import *
from apps.deptment.models import *
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
import datetime

class DailyWorkItemAdmin2(admin.ModelAdmin):
    list_display = ('dailywork','employee','role')
    model = DailyWorkItem
admin.site.register(DailyWorkItem, DailyWorkItemAdmin2)

class DailyWorkItemAdmin(admin.TabularInline):
    model = DailyWorkItem
    extra = 6

class DailyWorkAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'基本资料',{'fields': ['workingdate','project','place','car']}),
        (u'内容', {'fields': ['content'], 'classes': ['wide', 'extrapretty']}),
        (u'流程状态',{'fields': ['status']}),
      #  (u'统计情况',{'fields': ['how_many_people']}),
    ]

    list_display = ('workingdate','project','place','car','status','how_many_people','peoples_names')
    list_filter = ['workingdate','status']
    search_fields = ['project','dailyworkitem']
    inlines = [DailyWorkItemAdmin]

    #试用加入Admin的Action档
    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = u"一张派工单"
        else:
            message_bit = u"%s 张派工单 " % rows_updated
        self.message_user(request, u"成功发布%s 。" % message_bit)
    make_published.short_description = u"发布已选择的派工单"
    actions = [make_published]


    #http://docs.djangoproject.com/en/1.1/ref/contrib/admin/actions/#ref-contrib-admin-actions
    def export_selected_objects(modeladmin, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        ct = ContentType.objects.get_for_model(queryset.model)
        return HttpResponseRedirect("/export/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))


admin.site.register(DailyWork, DailyWorkAdmin)