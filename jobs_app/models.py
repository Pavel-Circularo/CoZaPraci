from django.db import models

# Create your models here.
class Job(models.Model):
    job_name = models.CharField()
    stereotype = models.TextField()
    reality = models.TextField()
    day_in_life = models.TextField()
    income = models.IntegerField()
    education = models.TextField()
    others = models.TextField()
    name = models.CharField(max_length=30)

