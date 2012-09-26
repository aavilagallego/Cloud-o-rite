from django.db import models

import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class SocialNetworks
class WebRoles(models.Model):
    role     = models.CharField(max_length=20, unique=True)
    desc     = models.CharField(max_length=300)

class Users(models.Model):
    user = models.OneToOneField(User)
    exp      = models.IntegerField()
    web      = models.CharField(max_length=150, null=True, blank=True)
    avatar   = models.ImageField(upload_to='avatars', null=True, blank=True)
    rol      = models.ManyToManyField(WebRoles)
    socials  = models.ManyToManyField(SocialNetworks, null=True, blank=True)
    ips      = models.ManyToManyField(UsersIp)
    clan     = models.ForeignKey(Clans, null=True, blank=True)


class Clans(models.Model):
    group    = models.CharField(max_length=20, unique=True)
    desc     = models.CharField(max_length=300)
    logo     = models.ImageField(upload_to='groups', null=True, blank=True)

class Powers(models.Model):
    power    = models.CharField(max_length=25, unique=True)
    desc     = models.CharField(max_length=150, null=True, blank=True)
    image    = models.ImageField(upload_to='powerups')

class ReadyPowers(models.Model):
    power = ForeignKey(Powers)
    user  = ForeignKey(Users)
    link  = ForeignKey(Links, null=True, blank=True)
    oDate = models.DateTimeField('Given Date')
    uDate = models.DateTimeField('Used Date')


class UsersIp(models.Model):
    date = models.DateTimeField('Date Used')
    ip   = models.CharField(max_length=45)

class Messages(models.Model):
    userFrom = models.ForeignKey(Users, related_name='userf')
    userTo   = models.ForeignKey(Users, related_name='usert')
    msg      = models.CharField(max_length=300)
    dateS = models.DateTimeField('Date Sent')
    dateR = models.DateTimeField('Date Readed', null=True, blank=True)
    spam  = models.ForeignKey(Users, null=True, blank=True)
    rUserF = models.BooleanField(null=True, blank=True)
    fUserT = models.BooleanField(null=True, blank=True)

class Shouts(models.Model):
    user = models.ForeignKey(Users)
    msg  = models.CharField(max_length='120')
    date = models.DateTimeField('Date Sent')
    spam = models.ForeignKey(Users)

class Links(models.Model):
    url    = models.CharField(max_length=300, unique=True)
    title  = models.CharField(max_length=100)
    desc   = models.CharField(max_length=500, null=True, blank=True)
    date   = models.DateTimeField('Date Added')
    datep  = models.DateTimeField('Date Published', null=True, blank=True)
    uvotes = models.ManyToManyField(Users, null=True, blank=True)
    avotes = models.ManyToManyField(UsersIp, null=True, blank=True)
    spam   = models.ManyToManyField(Users, null=True, blank=True)
    user   = models.ForeignKey(Users)
    status = models.ForeignKey(NewsStatus)
    via    = models.CharField(max_length=100, null=True, blank=True)
    tags   = models.ManyToManyField(Tags)

class NewsStatus(models.Model):
    name = models.CharField(max_length=20, unique=True)
    desc = models.CharField(max_length=300)


class Comments(models.Model):
    user = models.ForeignKey(Users)
    new  = models.ForeignKey(Links)
    text = models.CharField(max_length=800)
    votes= models.ManyToManyField(Users, null=True, blank=True)
    spam = models.ManyToManyField(Users, null=True, blank=True)


class Tags(models.Model):
    name = models.CharField(max_length=20, unique=True)
    desc = models.CharField(max_length=150, null=True, blank=True)


class Related(models.Model):
    new1  = models.ForeignKey(News, related_name='new1')
    new2  = models.ForeignKey(News, related_name='new2')
    user  = models.ForeignKey(Users)
    date  = models.DateTimeField('Date Added')
    score = models.IntegerField()

