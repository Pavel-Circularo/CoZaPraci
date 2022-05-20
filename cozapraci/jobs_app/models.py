from django.db import models

class Job(models.Model):
    job_name = models.CharField(max_length=30)
    stereotype = models.TextField()
    reality = models.TextField()
    day_in_life = models.TextField()
    income = models.CharField(max_length=150)
    education = models.TextField()
    others = models.TextField()
    name = models.CharField(max_length=30, blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.job_name}"