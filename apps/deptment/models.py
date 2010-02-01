#coding=utf-8

from django.db import models

#部门信息
class Deptment(models.Model):
    name = models.CharField('部门',max_length = 30)
    slug = models.SlugField(verbose_name='简写',max_length = 20,blank=True)

    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = u'部门'

    def __unicode__(self):
        return self.name




# 员工信息
class Employee(models.Model):
    #id = models.AutoField(primary_key = True)
    name = models.CharField('姓名',max_length = 20)
    slug = models.SlugField('简写',blank=True)
    position = models.CharField('职位',max_length = 20,blank=True)
    phone1 = models.CharField('电话',max_length=40,blank=True)
    deptment  = models.ForeignKey(Deptment,verbose_name='所属部门')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'员工'
        verbose_name_plural = u'员工'