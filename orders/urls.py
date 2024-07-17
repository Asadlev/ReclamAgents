from django.urls import path
from .views import OrderView, orders_thanks

app_name = 'orders'

urlpatterns = [
    path('order/', OrderView.as_view(), name='orders'),
    path('orders_thanks/', orders_thanks, name='orders_thanks')
]