from django.db import models

class Album(models.Model):
    title=models.CharField(max_length=50)
    artist=models.CharField(max_length=50)
    pic=models.FileField()
    ryear=models.CharField(max_length=4)
    genre=models.CharField(max_length=30)

class Song(models.Model):
    albid=models.ForeignKey(Album,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    file=models.FileField()
    
