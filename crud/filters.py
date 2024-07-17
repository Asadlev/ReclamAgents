from django_filters import FilterSet, CharFilter
from company.models import Company, Category
from django import forms

'''
Создаем свой набор фильтров для модели Product.
FilterSet, который мы наследуем,
должен чем-то напомнить знакомые вам Django-generic 
'''


class CompanyFilter(FilterSet):
    class Meta:
        model = Company
        fields = {
            # поиск по названию
            'name': ['icontains'],
        }



