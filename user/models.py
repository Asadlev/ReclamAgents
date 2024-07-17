from django.contrib.auth.models import AbstractUser
from django.db import models
from company.models import Company


class Employee(AbstractUser):
    ROLES = (
        ('admin', 'Администратор'),
        ('manager', 'Менеджер'),
        ('employee', 'Сотрудник'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='staff')
    image = models.ImageField(
        upload_to='employee_images',
        blank=True,
        null=True,
        verbose_name='Аватар',
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.username


class Client(models.Model):
    user = models.OneToOneField(Employee, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='client_images/', null=True, blank=True, verbose_name='Аватар')

    def __str__(self):
        return f'{self.user.username} - {self.company.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
