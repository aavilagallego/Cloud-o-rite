from django.db import models

import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class SocialNetworks(models.Model):
    name     = models.CharField(max_length=20)
    link     = models.CharField(max_length=150)
    username = models.CharField(max_length=30)

class WebRoles(models.Model):
    role     = models.CharField(max_length=20, unique=True)
    desc     = models.CharField(max_length=255)

class UsersIp(models.Model):
    date = models.DateTimeField('Date Used')
    ip   = models.CharField(max_length=45)

class Clans(models.Model):
    group    = models.CharField(max_length=20, unique=True)
    desc     = models.CharField(max_length=255)
    logo     = models.ImageField(upload_to='groups', null=True, blank=True)

class Users(models.Model):
    user     = models.OneToOneField(User)
    exp      = models.IntegerField()
    web      = models.CharField(max_length=150, null=True, blank=True)
    avatar   = models.ImageField(upload_to='avatars', null=True, blank=True)
    rol      = models.ManyToManyField(WebRoles)
    socials  = models.ManyToManyField(SocialNetworks, null=True, blank=True)
    ips      = models.ManyToManyField(UsersIp)
    clan     = models.ForeignKey(Clans, null=True, blank=True)

class Powers(models.Model):
    power    = models.CharField(max_length=25, unique=True)
    desc     = models.CharField(max_length=150, null=True, blank=True)
    image    = models.ImageField(upload_to='powerups')


class Messages(models.Model):
    userFrom = models.ForeignKey(Users, related_name='userf')
    userTo   = models.ForeignKey(Users, related_name='usert')
    msg      = models.CharField(max_length=255)
    dateS = models.DateTimeField('Date Sent')
    dateR = models.DateTimeField('Date Readed', null=True, blank=True)
    spam  = models.ForeignKey(Users, null=True, blank=True)
    rUserF = models.NullBooleanField(null=True, blank=True)
    fUserT = models.NullBooleanField(null=True, blank=True)

class Shouts(models.Model):
    user = models.ForeignKey(Users, related_name='sent_user')
    msg  = models.CharField(max_length='120')
    date = models.DateTimeField('Date Sent')
    votes= models.ForeignKey(Users, related_name='svoters')
    spam = models.ForeignKey(Users, related_name='sreporters')

class Tags(models.Model):
    name = models.CharField(max_length=20, unique=True)
    desc = models.CharField(max_length=150, null=True, blank=True)

class NewsStatus(models.Model):
    name = models.CharField(max_length=20, unique=True)
    desc = models.CharField(max_length=255)

class Links(models.Model):
    url    = models.CharField(max_length=255, unique=True)
    title  = models.CharField(max_length=100)
    desc   = models.CharField(max_length=500, null=True, blank=True)
    date   = models.DateTimeField('Date Added')
    datep  = models.DateTimeField('Date Published', null=True, blank=True)
    uvotes = models.ManyToManyField(Users, related_name='voters', null=True, blank=True)
    avotes = models.ManyToManyField(UsersIp, related_name='avoters', null=True, blank=True)
    spam   = models.ManyToManyField(Users, related_name='reporters', null=True, blank=True)
    user   = models.ForeignKey(Users,  related_name='sender')
    status = models.ForeignKey(NewsStatus)
    via    = models.CharField(max_length=100, null=True, blank=True)
    tags   = models.ManyToManyField(Tags)

class ReadyPowers(models.Model):
    power = models.ForeignKey(Powers)
    user  = models.ForeignKey(Users)
    link  = models.ForeignKey(Links, null=True, blank=True)
    oDate = models.DateTimeField('Given Date')
    uDate = models.DateTimeField('Used Date')



class Comments(models.Model):
    user = models.ForeignKey(Users, related_name='cuser')
    link = models.ForeignKey(Links, related_name='comments_on')
    text = models.CharField(max_length=800)
    votes= models.ManyToManyField(Users, related_name='cvoters', null=True, blank=True)
    spam = models.ManyToManyField(Users, related_name='creporters', null=True, blank=True)

class Related(models.Model):
    new1  = models.ForeignKey(Links, related_name='new1')
    new2  = models.ForeignKey(Links, related_name='new2')
    user  = models.ForeignKey(Users)
    date  = models.DateTimeField('Date Added')
    score = models.IntegerField()

