from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Battery, BatteryModel

# Create your views here.


def battery_list(request):
    battery_list = list(Battery.objects.all())
    # print(battery_list)
    # output = ', '.join(
    #     [battery.battery_owner.company_name for battery in battery_list])
    # print(output)
    context = {'battery_list': battery_list}
    return render(request, 'battery/batteryList.html', context)
    # return HttpResponse(output)
