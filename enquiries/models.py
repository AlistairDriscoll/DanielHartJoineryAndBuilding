from django.db import models


class Enquiry(models.Model):
    """ For the enquiry model """

    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    location = models.CharField(max_length=120, blank=False)
    job_title = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.location} — {self.job_title}"
