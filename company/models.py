from django.db import models
from django.urls import reverse


class Category(models.Model):
    CATEGORY_CHOICE = (
        ('Corporation', 'Корпорация'),
        ('Company', 'Компания'),
        ('Firms', 'Фирма'),
    )
    name = models.CharField(max_length=120, choices=CATEGORY_CHOICE, default='Company', unique=True, verbose_name='Категория')
    slug = models.SlugField(max_length=120, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Company(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название Компании')
    slug = models.SlugField(max_length=120, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(unique=True, blank=True, null=False, verbose_name='Описание')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес')
    contact_info = models.CharField(max_length=20, verbose_name='Номер телефона')
    unique_code = models.CharField(max_length=5, unique=True, verbose_name='Уникальный код')
    image = models.ImageField(upload_to='company_images/', null=True, blank=True, verbose_name='Изображение компании')
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, verbose_name='Категория компании')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - Категория: {self.category.name}'

    def get_absolute_url(self):
        return reverse('crud:detail_company', kwargs={'company_slug': self.slug})

    def display_id(self):
        return f'{self.id:04}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


