#coding=utf-8
from django.db import models
from apps.deptment.models import *

#工程状态
PROJECTSTATE_CHOISES=(
        ('正常','正常'),
        ('完成','完成'),
        ('关闭','关闭'),
)

# 工程信息
class Project(models.Model):
    name = models.CharField(u'项目',max_length=100)
    wbs  = models.CharField('wbs元素',max_length = 30,blank=True,null=True)
    designnumber = models.CharField('设计编号',max_length = 30,blank=True,null=True)
    innernumber  = models.CharField('内部编号',max_length = 30,blank=True,null=True)
    budget  = models.IntegerField('预算自购材料金额',blank=True)
    deptment = models.ForeignKey(Deptment,verbose_name='所属部门',blank=True,null=True)
    projectstate = models.BooleanField('是否关闭',default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'项目'
        verbose_name_plural = u'项目'