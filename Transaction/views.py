from django.shortcuts import render
from .models import Transaction
from django.template import loader
# Create your views here.


def transaction_list(request):
    transaction_list = list(Transaction.objects.all())
    context = {'transaction_list': transaction_list}
    return render(request, 'transaction/transactionList.html', context)
