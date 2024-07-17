from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from company.models import Company, Category
from .models import Employee, Client
from .forms import (
    EmployeeLoginForm, ClientLoginForm, EmployeeRegistrationForm, ClientRegistrationForm,
    EmployeeProfileForm, ClientProfileForm
)


def choose_user_type(request):
    return render(request, 'user/choose_user_type.html')


def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            messages.success(request, 'Успешная регистрация и вход')
            return redirect('user:profile_employee')
    else:
        form = EmployeeRegistrationForm()

    context = {
        'title': 'Регистрация сотрудника',
        'form': form,
    }
    return render(request, 'user/register_employee.html', context)


def register_client(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            messages.success(request, 'Успешная регистрация и вход')
            return redirect('user:profile_client')
    else:
        form = ClientRegistrationForm()

    context = {
        'title': 'Регистрация клиента',
        'form': form,
    }
    return render(request, 'user/register_client.html', context)


def login_employee(request):
    if request.method == 'POST':
        form = EmployeeLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.role in ['admin', 'manager', 'employee']:
                auth.login(request, user)
                messages.success(request, 'Вы вошли в аккаунт.')
                return redirect('user:profile_employee')
            else:
                messages.error(request, 'Этот пользователь не является сотрудником.')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    else:
        form = EmployeeLoginForm()

    context = {
        'title': "Авторизация сотрудника",
        'form': form,
    }
    return render(request, 'user/login_employee.html', context)


def login_client(request):
    if request.method == 'POST':
        form = ClientLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                if hasattr(user, 'client'):
                    auth.login(request, user)
                    messages.success(request, 'Вы вошли в аккаунт.')
                    return redirect('user:profile_client')
                else:
                    messages.error(request, 'Этот пользователь не является клиентом.')
            else:
                messages.error(request, 'Неверное имя пользователя или пароль.')
        else:
            messages.error(request, 'Ошибка валидации формы.')
    else:
        form = ClientLoginForm()

    context = {
        'title': "Авторизация клиента",
        'form': form,
    }
    return render(request, 'user/login_client.html', context)


@login_required
def profile_employee(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = EmployeeProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлен.')
            return redirect('user:profile_employee')
    else:
        form = EmployeeProfileForm(instance=request.user)

    context = {
        'title': 'Профиль сотрудника',
        'form': form,
        'categories': categories,
    }

    return render(request, 'user/profile_employee.html', context)


@login_required
def profile_client(request):
    categories = Category.objects.all()
    try:
        client = request.user.client
    except Client.DoesNotExist:
        client = None

    if request.method == 'POST':
        form = ClientProfileForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлен.')
            return redirect('user:profile_client')
    else:
        form = ClientProfileForm(instance=client)

    context = {
        'title': 'Профиль клиента',
        'form': form,
        'categories': categories,
    }

    return render(request, 'user/profile_client.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home:home'))
