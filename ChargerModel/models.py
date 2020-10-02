from django.db import models
from Company.models import Company

# Create your models here.


class ChargerModel(models.Model):
    charger_model_no = models.CharField(max_length=200)
    charger_model_oem = models.ForeignKey(Company, on_delete=models.RESTRICT)
    charger_model_voltage = models.DecimalField(
        decimal_places=10, max_digits=20)
    charger_model_current = models.DecimalField(
        decimal_places=10, max_digits=20)
    charger_model_width = models.DecimalField(decimal_places=10, max_digits=20)
    charger_model_length = models.DecimalField(
        decimal_places=10, max_digits=20)
    charger_model_height = models.DecimalField(
        decimal_places=10, max_digits=20)
    charger_connector_no = models.IntegerField()
    charger_model_firmware_version_latest = models.CharField(max_length=20)
    # charger_model_firmware_version_list = models.ManyToManyField(Firmware)

    def __str__(self):
        return self.charger_model_no


# class Firmware(models.Model):
#     firmware_version = models.CharField(max_length=20)
#     firmware_charger_model = models.ForeignKey(
#         ChargerModel, on_delete=models.RESTRICT)
