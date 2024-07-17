from datetime import datetime
from django.core.mail import send_mail, mail_admins, mail_managers
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic import ListView
from .models import Order


class OrderView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'orders/company_orders.html')

    def post(self, request, *args, **kwargs):
        orders = Order(
            date=datetime.strptime(request.POST['date'], "%Y-%m-%d"),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
            email=request.POST['email'],
        )
        orders.save()

        send_mail(
            subject=f'{orders.client_name}: {orders.date.strftime("%S-%m-%d")}',
            message=orders.message,
            from_email='imaralievasadbek@yandex.ru',
            recipient_list=[orders.email]

        )
        return redirect('orders:orders_thanks')


def orders_thanks(request):
    return render(request, 'orders/orders_thanks.html')
