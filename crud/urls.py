from django.urls import path
from .views import CreateCompanyView, UpdateCompanyView, DeleteCompanyView, DetailCompanyView


app_name = 'crud'


urlpatterns = [
    path('create_company/', CreateCompanyView.as_view(), name='create_company'),
    path('update_company/<slug:company_slug>/', UpdateCompanyView.as_view(), name='update_company'),
    path('delete_company/<slug:company_slug>/', DeleteCompanyView.as_view(), name='delete_company'),
    path('detail_company/<slug:company_slug>/', DetailCompanyView.as_view(), name='detail_company'),
]