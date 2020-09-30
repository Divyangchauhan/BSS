from django.db import models
from Company.models import Company

# Create your models here.


class BatteryModel(models.Model):
    battery_model_no = models.CharField(max_length=100)
    battery_model_oem = models.ForeignKey(Company, on_delete=models.CASCADE)
    battery_model_capacity = models.DecimalField(
        decimal_places=10, max_digits=20)
    battery_model_current = models.DecimalField(
        decimal_places=10, max_digits=20)
    battery_model_voltage = models.DecimalField(
        decimal_places=10, max_digits=20)
    battery_model_width = models.DecimalField(decimal_places=10, max_digits=20)
    battery_model_length = models.DecimalField(
        decimal_places=10, max_digits=20)
    battery_model_height = models.DecimalField(
        decimal_places=10, max_digits=20)

    def __str__(self):
        return self.battery_model_no
