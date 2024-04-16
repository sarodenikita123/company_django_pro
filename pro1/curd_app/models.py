from django.db import models


class Company(models.Model):
    type = [("CM", "campaign management"), ("CRM", "CRM Administrations"), ("ED", "Email Development"), ("Emp", "Employee"), ("PT", "Partner")]
    Title = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)
    job_function = models.CharField(max_length=20, choices=type, default=True)
    training_date = models.DateField()
    dietary_requirement = models.CharField(max_length=20)
    exceptions = models.CharField(max_length=20)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)



