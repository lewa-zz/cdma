#coding=utf-8
## TODO: 派工人员统计末完成

from django.db import models
from datetime import datetime

from apps.project.models import *
from apps.deptment.models import *
from apps.car.models import *

WORKINGROLE_CHOISES=(
        (u'领队',u'领队'),
        (u'安全员',u'安全员'),
        (u'施工员',u'施工员'),
        (u'兼职司机',u'兼职司机')
)

#每日派工单
class DailyWork(models.Model):
    STATUS_CHOICES = (
        ('d', u'草稿'),
        ('p', u'发布'),
        ('w', u'已回单'),
    )

    workingdate = models.DateField(u'派工日', editable=True,default=datetime.now)
    project     = models.ForeignKey(Project,verbose_name = '所属工程')
#    deptment    = modes.ForeignKey(Deptment,verbose_name = '派工部门')
    place       = models.CharField('工作地点',max_length = 100,help_text='请输入工作地点，注意不能为空')
    content     = models.TextField('工作内容',help_text='请输入工作内容，注意不能为空')
    car         = models.ForeignKey(Car,verbose_name = '车辆',blank=True,null=True,help_text='派出的车辆')
    overtime    = models.IntegerField('超时加班数',default = 0)
    other       = models.TextField('其他',blank=True,null=True)
    status      = models.CharField('状态',max_length=1, choices=STATUS_CHOICES)

    def __unicode__(self):
        return "DailyWork.workingdate"

    #计算派工单出勤人数
    def how_many_people(self):
        detail = self.dailyworkitem_set.all()
        return detail.count()
    how_many_people.short_description = u'人数'

    #把派工明细人员名字列成一串字符以备显示
    def peoples_names(self):
        t=""
        details = self.dailyworkitem_set.all()
        for po in details:
            t += str(po)+" "
        return t
    peoples_names.short_description = u'出勤人员'

    class Meta:
        verbose_name = u'派工单'
        verbose_name_plural = u'派工单'

#每日派工单，派出的资源明细
class DailyWorkItem(models.Model):
    dailywork     = models.ForeignKey(DailyWork,verbose_name = '派工单')
    employee      = models.ForeignKey(Employee,verbose_name = '员工')
    role          = models.CharField('担任', max_length=10,choices=WORKINGROLE_CHOISES,
                    blank=True,null=True,help_text='人员所担任的角色')

    def __unicode__(self):
        return self.employee.name

    class Meta:
        unique_together = ("dailywork",  "employee")
        verbose_name = u'派出人员明细'
        verbose_name_plural = u'派出人员明细'
