from django.db import models


class Channels(models.Model):
    Channels_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.Channels_name


class Category(models.Model):
    Category_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.Category_name


class Video(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    key = models.CharField(max_length=100, unique=True)
    channel = models.ManyToManyField('Channels', related_name='Video')
    categories = models.ManyToManyField('Category', related_name='Video')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " | " + str(self.id)
