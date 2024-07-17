
from django.urls import path
from .views import CompanyListView

app_name = 'company'

urlpatterns = [
    path('company/', CompanyListView.as_view(), name='company_list'),
    path('company_sorted/<str:company_slug>/', CompanyListView.as_view(), name='company_categories'),
    path('search/', CompanyListView.as_view(), name='search'),
]




