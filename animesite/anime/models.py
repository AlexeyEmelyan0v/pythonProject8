from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Studio(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateTimeField('birth_date')
    image = models.FileField(upload_to="", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('anime:director_info', args=[self.id])

class Anime(models.Model):
    title = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    release_date = models.DateTimeField('release_date')
    image = models.FileField(upload_to="", blank=True, null=True)
    viewers = models.ManyToManyField(User, null=True, blank=True)
    description = models.CharField(max_length=3000, blank=True, null=True)
    link = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('anime:anime_info', args=[self.id])

# Create your models here.