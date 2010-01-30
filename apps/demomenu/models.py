#coding=utf-8

from django.db import models
from django.contrib.auth.models import User

class Province(models.Model):
    name = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length = 50)
    province = models.ForeignKey(Province, related_name = "cities")

    def __unicode__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length = 50)
    city = models.ForeignKey(City, related_name = "schools")

    def __unicode__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, related_name = "profile")
    province = models.ForeignKey(Province, verbose_name = u'所在省', related_name = "profiles", null = True, blank = True)
    city = models.ForeignKey(City, verbose_name = u'所在城市', related_name = "profiles", null = True, blank = True)
    school = models.ForeignKey(School, verbose_name = u'所在学校', related_name = "profiles", null = True, blank = True)

    def __unicode__(self):
        return self.user.username
