from django.db import models


class Enquiry(models.Model):
    """ For the enquiry model """

    name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=120)
    job_title = models.CharField(max_length=120)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.location} — {self.job_title}"
