#coding=utf-8
from django.db import models
from apps.deptment.models import *

#车辆种类
CARTYPE_CHOISES=(
        (u'工程车',u'工程车'),
        (u'人货车',u'人货车'),
        (u'小轿车',u'小轿车'),
)


# 车辆信息
class Car(models.Model):
    carnumber = models.CharField(u'车牌',max_length=30,unique=True)
    driver  = models.CharField('司机',max_length = 30,blank=True,null=True)
    phone   = models.CharField('电话',max_length = 30,blank=True,null=True)
    type    = models.CharField('车型',max_length=10,choices=CARTYPE_CHOISES,
                    blank=True,null=True,help_text='车辆类型')
    islend  = models.BooleanField('是否租车',default=False)
    cost    = models.IntegerField('每天使用金额',default = 0)

    def __unicode__(self):
        return self.carnumber

    class Meta:
        verbose_name = u'车辆'
        verbose_name_plural = u'车辆'

class CarDaily(models.Model):
    workingdate = models.DateField('派工日')
    car         = models.ForeignKey(Car,verbose_name = '车辆',unique_for_date='workingdate')
    deptment    = models.ForeignKey(Deptment,verbose_name='部门')
    place       = models.CharField('工作地点',max_length = 100,blank=True,null=True)

    def __unicode__(self):
        return u'%s派出%s车辆到%s专业'%(self.workingdate,self.car.__unicode__(),self.deptment.__unicode__())

    class Meta:
        verbose_name = u'派车明细'
        verbose_name_plural = u'派车明细'
