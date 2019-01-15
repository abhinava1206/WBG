from django.db import models

# Create your models here.

class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    statistics = models.TextField(default = '{}')
    achievements = models.TextField(default='[]')
    class Meta():
        ordering = ('-created',)
    def __str__(self):
        return self.username

class Match(models.Model):
    players = models.ManyToManyField(Profile)
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.TimeField(blank=True)
    statistics = models.TextField(default = '{}')
