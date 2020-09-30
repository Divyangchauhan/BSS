from django.db import models


# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=20, unique=True)
    company_city = models.CharField(max_length=20)
    company_state = models.CharField(max_length=20)
    company_country = models.CharField(
        max_length=20, choices=(('India', 'India'), ('USA', 'US'), ('UK', 'UK')), default="India")

    def __str__(self):
        return self.company_name
