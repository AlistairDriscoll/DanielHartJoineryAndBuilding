from django.db import models


class Skill(models.Model):
    """ Made so the skillset can easily be modified """

    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
