

from django.urls import path
from .views import base, about_us

app_name = 'home'

urlpatterns = [
    path('', base, name='home'),
    path('about_us/', about_us, name='about_us'),
]
