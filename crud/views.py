from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from company.models import Company
from company.forms import CompanyForm


class DetailCompanyView(DetailView):
    model = Company
    context_object_name = 'company'
    template_name = 'crud/detail_company.html'
    success_url = reverse_lazy('company:company_list')

    slug_field = 'slug'
    slug_url_kwarg = 'company_slug'


class CreateCompanyView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'crud/create_company.html'

    def get_success_url(self):
        return reverse_lazy('crud:detail_company', kwargs={'company_slug': self.object.slug})


    slug_field = 'slug'
    slug_url_kwarg = 'company_slug'


class UpdateCompanyView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'crud/update_company.html'

    def get_success_url(self):
        return reverse_lazy('crud:detail_company', kwargs={'company_slug': self.object.slug})

    slug_field = 'slug'
    slug_url_kwarg = 'company_slug'


class DeleteCompanyView(DeleteView):
    model = Company
    template_name = 'crud/delete_company.html'
    success_url = reverse_lazy('company:company_list')

    slug_field = 'slug'
    slug_url_kwarg = 'company_slug'


