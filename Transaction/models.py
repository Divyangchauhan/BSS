from django.db import models
from Battery.models import Battery
from Station.models import Station


# Create your models here.

class Transaction(models.Model):
    transaction_start_time = models.DateTimeField()
    transaction_stop_time = models.DateTimeField()
    transaction_day = models.DateField()
    Battery = models.ForeignKey(
        Battery, on_delete=models.CASCADE)
    Station = models.ForeignKey(
        Station, on_delete=models.CASCADE)
    battery_state_in = models.IntegerField()
    battery_state_out = models.IntegerField()

    @property
    def battery_charged(self):
        return (self.battery_state_out - self.battery_state_in)

    @property
    def transaction_amount(self):
        return self.battery_charged(self)*ChargeRate()


def ChargeRate():
    chargingrate = 1
    return chargingrate
