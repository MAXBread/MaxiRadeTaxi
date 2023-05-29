from django.urls import path
from . import views


urlpatterns = [
    path('', views.operator, name='operator'),
    path('order', views.order, name='order'),
    path('driver', views.new_driver, name='driver'),
    path('order/<int:pk>', views.OrderUpdateView.as_view(), name='order-update'),
    path('driver/<int:pk>', views.DriverUpdateView.as_view(), name='driver-update')

]