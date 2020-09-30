from django.db import models
from Battery.models import Battery
from Station.models import Station
from Transaction.models import Transaction


# Create your models here.

class Bill(models.Model):
    bill_to = models.CharField(max_length=100)
    bill_transactions = models.ManyToManyField(Transaction)

    @property
    def Bill_amount(self):
        bill_amount = 0
        for i in self.bill_transactions.all():
            bill_amount = bill_amount + self.transaction_amount
