from django.db import models
from Company.models import Company
from ChargerModel.models import ChargerModel

STATUS = (
    ('available', 'Available to borrow'),
    ('charging', 'Charging in Charger'),
    ('archived', 'Archived - not available anymore'),
)


# Create your models here.
class Charger(models.Model):
    charger_SN = models.CharField(max_length=200)
    charger_model = models.ForeignKey(ChargerModel, on_delete=models.RESTRICT)
    charger_longitude = models.DecimalField(decimal_places=10, max_digits=20)
    charger_latitude = models.DecimalField(decimal_places=10, max_digits=20)
    charger_firmware_version = models.CharField(max_length=20)
    charger_owner = models.ForeignKey(
        Company, on_delete=models.CASCADE, blank=True, null=True)
    charger_status = models.CharField(
        max_length=10, choices=STATUS, default='available')

    def __str__(self):
        return self.charger_SN
