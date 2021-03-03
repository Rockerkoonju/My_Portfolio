from django.db import models

class Channels(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        retrun self.name

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        retrun self.name
        
class Video(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    key = models.CharField(max_length=100, unique=True)
    channel = models.ManyToManyField('Channels', related_name='Video')
    categories = models.ManyToManyField('Category', related_name='Video')
    
    def __str__(self):
        return self.title + " | " + self.id
