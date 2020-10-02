from django.db import models
from Battery.models import Battery
from Station.models import Station
from Charger.models import Charger

# Create your models here.


def ChargeRate(transaction):
    chargingrate = 1
    print(transaction)
    return chargingrate


class Transaction(models.Model):
    transaction_start_time = models.DateTimeField()
    transaction_stop_time = models.DateTimeField()
    transaction_day = models.DateField()
    Battery = models.ForeignKey(
        Battery, on_delete=models.CASCADE)
    Station = models.ForeignKey(
        Station, on_delete=models.CASCADE)
    Charger = models.ForeignKey(Charger, on_delete=models.RESTRICT)
    battery_state_in = models.IntegerField()
    battery_state_out = models.IntegerField()

    @property
    def battery_charged(self):
        return (self.battery_state_out - self.battery_state_in)

    @property
    def transaction_amount(self):
        return self.battery_charged*ChargeRate(self)

    def __str__(self):
        return str(self.id)
