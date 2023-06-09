from django.db import models


# Create your models here.
class Movies(models.Model):
    posters = models.URLField()
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    rating = models.FloatField()


class TVShows(models.Model):
    posters = models.URLField()
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    rating = models.FloatField()

    def __repr__(self):
        return f'{self.title} {self.year}'
