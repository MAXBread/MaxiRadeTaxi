import django_tables2 as tables
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import OrderForm, DriverForm
from .models import Drivers, Orders
from django_tables2.utils import A  # alias for Accessor


class DriversTable(tables.Table):
    car_number = tables.LinkColumn("driver-update", args=[A("pk")])

    class Meta:
        model = Drivers


class OrdersTable(tables.Table):
    phone = tables.LinkColumn("order-update", args=[A("pk")])

    class Meta:
        model = Orders


def operator(request):
    if not request.user.is_authenticated:
        return redirect('login')
    drivers_table = DriversTable(Drivers.objects.all(), prefix='driver-')
    orders_table = OrdersTable(Orders.objects.all(), prefix='order-')

    if 'driver-sort' in request.GET.keys():
        drivers_table.order_by = request.GET['driver-sort']
    else:
        drivers_table.order_by = 'status'

    if 'order-sort' in request.GET.keys():
        orders_table.order_by = request.GET['order-sort']
    else:
        orders_table.order_by = 'status'

    return render(request, 'oper/operator.html', {'drivers_table': drivers_table, 'orders_table': orders_table})


def order(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('operator')
        else:
            error = 'form error'

    form = OrderForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'oper/order.html', data)


def new_driver(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ''
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('operator')
        else:
            error = 'form error'

    form = DriverForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'oper/driver.html', data)


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    redirect_field_name = None
    model = Orders
    template_name = 'oper/order.html'
    form_class = OrderForm


class DriverUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    redirect_field_name = None
    model = Drivers
    template_name = 'oper/driver.html'
    form_class = DriverForm
