from django.db import models
from django.utils import timezone

class Job(models.Model):
    url = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    company_link = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    ratings = models.CharField(max_length=100)
    reviews = models.CharField(max_length=250)
    experience = models.CharField(max_length=250)
    salary = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    posted = models.CharField(max_length=250)
    skills = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created_date']

    class Admin:
        pass

class Company(models.Model):
    company_link = models.CharField(max_length=250, unique=True)
    company_name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    
    def __str__(self):
        return self.company_name
    
    class Meta:
        ordering = ['company_name']

    class Admin:
        pass

# Create your models here.
