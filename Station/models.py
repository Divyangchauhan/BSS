from django.db import models
from Company.models import Company


# Create your models here.

class Station(models.Model):
    station_name = models.CharField(max_length=20)
    station_longitude = models.IntegerField()
    station_latitude = models.IntegerField()
    station_owner = models.ForeignKey(Company, on_delete=models.CASCADE)
    station_city = models.CharField(max_length=20)
    station_state = models.CharField(max_length=20)
    station_country = models.CharField(
        max_length=20, choices=(('India', 'India'), ('USA', 'US'), ('UK', 'UK')), default="India")

    def __str__(self):
        return self.station_name
