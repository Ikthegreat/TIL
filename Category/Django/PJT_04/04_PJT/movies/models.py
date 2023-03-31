from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.CharField(max_length=50)
    description = models.TextField()
    actor_image = models.ImageField(height_field=None, width_field=None, max_length=None, blank=True)