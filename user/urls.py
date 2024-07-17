from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('choose_user_type/', views.choose_user_type, name='choose_user_type'),
    path('register_employee/', views.register_employee, name='register_employee'),
    path('register_client/', views.register_client, name='register_client'),
    path('login_employee/', views.login_employee, name='login_employee'),
    path('login_client/', views.login_client, name='login_client'),
    path('profile_employee/', views.profile_employee, name='profile_employee'),
    path('profile_client/', views.profile_client, name='profile_client'),
    path('logout/', views.logout, name='logout'),
]
