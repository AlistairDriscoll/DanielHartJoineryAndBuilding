from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class CATReview(models.Model):
    """ Model for previous reviews on Checkatrade """

    title = models.CharField(max_length=100)
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    description = models.TextField()
    location = models.CharField(max_length=7, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title


class PastWorkAlbum(models.Model):
    """ Model where my uncle can upload pictures of previous jobs """

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    """ Any amount of images allowed for PastWorkAlbum so made its own model"""

    album = models.ForeignKey(
        PastWorkAlbum,
        on_delete=models.CASCADE,
        related_name='images'
    )

    def __str__(self):
        return f"Image for {self.album.title}"
