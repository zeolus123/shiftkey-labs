from __future__ import unicode_literals

from django.db import models
import tweepy

class SavedTweet(models.Model):
    id_str = models.CharField(max_length=30)
    text = models.TextField(max_length=140)
    created_at = models.CharField(max_length=100)
    owner = models.CharField(max_length=100, default=" ")

    def __str__(self):
        return self.text

class SavedUser(models.Model):
    source = models.CharField(max_length=16)
    handle = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    influencer = models.CharField(max_length=16)
    followers = models.IntegerField()
    following = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.handle
    
