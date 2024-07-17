from django.shortcuts import render
from django.views.generic import ListView
from company.models import Company, Category
from crud.filters import CompanyFilter


class CompanyListView(ListView):
    model = Company
    context_object_name = 'companies'
    template_name = 'company/list_company.html'
    paginate_by = 15

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        query = self.request.GET.get('q', None)

        if category_slug == 'all' or category_slug is None:
            if query:
                queryset = Company.objects.filter(name__icontains=query)
            else:
                queryset = Company.objects.all()
        else:
            if query:
                queryset = Company.objects.filter(name__icontains=query, category__slug=category_slug)
            else:
                queryset = Company.objects.filter(category__slug=category_slug)

        self.filterset = CompanyFilter(self.request.GET, queryset)
        queryset = self.filterset.qs

        ordering = self.request.GET.get('ordering')
        if ordering:
            queryset = queryset.order_by(ordering)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['slug_url'] = self.kwargs.get('category_slug')
        context['search_query'] = self.request.GET.get('q', None)
        return context
