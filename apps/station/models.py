#coding=utf-8

from django.db import models
from apps.deptment.models import *

# 基站种类 model
class Category(models.Model):
    name = models.CharField(u'基站种类',max_length=20)
    
    class Meta:
        verbose_name = u'基站种类'  
        verbose_name_plural = u'基站种类'  

    def __unicode__(self):
        return self.name

STATIONSTATE_CHOISES=(
        ('D','取消'),
        ('N','正常'),
        ('F','完成'),
)

TRANSTYPE_CHOISES=(
        ('新建站','新建站'),
        ('扩容站','扩容站'),
        ('室分','室分'),
)

TRANSGUAGE_CHOISES = (
        (0,u'末开工'),
        (1,u'立机柜'),
        (2,u'布放电源'),
        (3,u'调测中'),
        (4,u'调测完'),
        (5,u'资料录入'),
        (6,u'初验'),
)

DEVICETYPE_CHOISES = (
        ('Metro1000','Metro1000'),
        ('Metro100','Metro100'),
        ('Metro500','Metro500'),
        ('Metro3000','Metro3000'),
        ('Metro5000','Metro5000'),
        ('OSN3500','OSN3500'),
        ('OSN7500','OSN7500'),
        ('OSN9500','OSN9500'),
)

# 基站抽象类 Model
class CommonStation(models.Model):
    name = models.CharField('站名',max_length=100)
    slug = models.SlugField('站号',blank=True)
    area = models.CharField('镇区',max_length=10,blank=True)
    longitude = models.CharField('经度',max_length=20,blank=True)
    latitude  = models.CharField('纬度',max_length=20,blank=True)
    addr = models.TextField('地址',default='',blank=True)
    maintain  = models.CharField('代维公司',max_length = 20,blank=True)
    category = models.ForeignKey(Category,verbose_name='基站种类',
                    related_name="stations_related",blank=True)
   #ForeignKey,ManyToManyField时的related_name属性, 必须为它指定一个对于所有子类都唯一的反向引用的名字
   # m2m = models.ManyToMany(OtherModel, related_name="station_related")

    def __unicode__(self):
        return self.name

    class Meta:
#        abstract = True
        verbose_name = u'基站'
        verbose_name_plural = u'基站'


#新建基站
class NewlyStation(CommonStation):
    bselfbuild      = models.BooleanField('是否公司无线负责')
    
    class Meta:
       verbose_name = u'新建基站'
       verbose_name_plural = u'新建基站'
    

#扩容基站
class ExtStation(CommonStation):
    belongto = models.CharField(u'归属', choices=(('C','电信'), ('U','联通')), 
         max_length=1)
    class Meta:
        verbose_name = u'扩容基站'
        verbose_name_plural = u'扩容基站'
        

#室分基站
class IndoorStation(CommonStation):
    cond = models.CharField('施工条件',max_length=20,blank=True)
    class Meta:
        verbose_name = u'室分基站'
        verbose_name_plural = u'室分基站'
    

#基站扩容传输信息
class TransInfo(models.Model):
    station    = models.OneToOneField(CommonStation,verbose_name='站点')
    device     = models.CharField(verbose_name='设备类型', max_length=20, choices=DEVICETYPE_CHOISES)
    cabinhight          = models.CharField('机柜情况',max_length = 20,blank=True)
    needaddcross        = models.NullBooleanField('是否新增走线架')
    crossfinisheddate   = models.DateField(verbose_name='走线架完成日期',blank=True)
    transtype           = models.CharField(verbose_name='站点传输类型', max_length=20, choices=TRANSTYPE_CHOISES)
    belongproject       = models.CharField('所在工程',max_length = 20)
    belongset           = models.PositiveSmallIntegerField('批次')
    labelinfo           = models.CharField('标签粘贴情况',max_length = 20)
    glidenumber         = models.CharField('流水号',max_length = 20)
    upperdevice         = models.CharField('上联设备',max_length = 20)
    upperdeviceport     = models.CharField('上联设备端口',max_length = 20)
    resinfo             = models.CharField('资源录入',max_length = 20)
    
    adddate    = models.DateField('更新日')
    transguage  = models.PositiveSmallIntegerField(verbose_name='进度',
                         choices=TRANSGUAGE_CHOISES,default=None)      
    employee    = models.ForeignKey(Employee,verbose_name='施工人员',blank=True)
    
    employee1 = models.CharField('其他人员信息',max_length=50,blank=True)
    
    descript    = models.TextField('进度描述')
    
    class Meta:
        verbose_name = u'传输信息'
        verbose_name_plural = u'传输信息'

    def __unicode__(self):
        return self.cabinhight


class TransDetail(models.Model):
    station     = models.ForeignKey(CommonStation,verbose_name='站点',unique_for_date='adddate')
    adddate    = models.DateField('更新日')   
    transguage  = models.PositiveSmallIntegerField(verbose_name='进度',
                         choices=TRANSGUAGE_CHOISES,default=None)
    employee    = models.ForeignKey(Employee,verbose_name='施工人员')
    descript    = models.TextField('进度描述',blank=True,null=True)
    
    class Meta:
        verbose_name = u'传输进度明细'
        verbose_name_plural = u'传输进度明细'
        get_latest_by = "adddate"
            
    def __unicode__(self):
        return 'self.descript'