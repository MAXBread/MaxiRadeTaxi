from django.shortcuts import render
from .models import Drivers, Orders
from .forms import OrderForm

import django_tables2 as tables

from django.http import HttpResponse


class DriversTable(tables.Table):
    class Meta:
        model = Drivers


class OrdersTable(tables.Table):
    class Meta:
        model = Orders


def operator(request):
    drivers = Drivers.objects.order_by('status')
    drivers_table = DriversTable(drivers)
    orders_table = OrdersTable(Orders.objects.order_by('status'))
    #fields_dict = {field.name: field.verbose_name for field in Drivers._meta.get_fields()}

    #return HttpResponse("<h4>Hello world</h4>")
    return render(request, 'oper/operator.html', {'drivers_table': drivers_table, 'orders_table': orders_table})


def order(request):
    form = OrderForm()

    data = {
        'form': form
    }
    return render(request, 'oper/order.html', data)

