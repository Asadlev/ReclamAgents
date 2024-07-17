from django.shortcuts import render


def base(request):
    return render(request, 'home/base.html')


def about_us(request):
    return render(request, 'home/about_us.html')




