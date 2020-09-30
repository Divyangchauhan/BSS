from django.db import models
from Company.models import Company
from BatteryModel.models import BatteryModel

STATUS = (
    ('available', 'Available to borrow'),
    ('borrowed', 'Borrowed by someone'),
    ('charging', 'Charging in Charger'),
    ('archived', 'Archived - not available anymore'),
)


# Create your models here.
class Battery(models.Model):
    battery_SN = models.CharField(max_length=200)
    battery_model = models.ForeignKey(BatteryModel, on_delete=models.RESTRICT)
    battery_longitude = models.DecimalField(decimal_places=10, max_digits=20)
    battery_latitude = models.DecimalField(decimal_places=10, max_digits=20)
    battery_owner = models.ForeignKey(
        Company, on_delete=models.CASCADE, blank=True, null=True)
    battery_status = models.CharField(
        max_length=10, choices=STATUS, default='available')

    def __str__(self):
        return self.battery_SN
