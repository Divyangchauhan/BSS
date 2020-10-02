from django.urls import path

from . import views

urlpatterns = [
    path('battery_list', views.battery_list, name='battery_list'),
    path('<int:battery_SN>/battery_detail',
         views.battery_detail, name='battery_detail'),
]
