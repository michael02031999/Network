from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    pass

class All_Post(models.Model): 
    id = models.IntegerField(primary_key=True)
    username = models.TextField(max_length=500)
    comment = models.TextField(max_length=500)
    date = models.TextField(max_length=500)
    time = models.TextField(max_length=500)
    datetime = models.DateTimeField(blank=True, default=datetime.now)
    likes = models.IntegerField()

class Following_Follower(models.Model):
    username = models.TextField(max_length=500)
    following = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)

class following_system(models.Model):
    follower = models.TextField(max_length=500)
    leader = models.TextField(max_length=500)

class liked_system(models.Model):
    liker = models.TextField(max_length=500)
    receiverId = models.IntegerField(max_length=500)