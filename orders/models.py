from datetime import datetime

from django.db import models


class Order(models.Model):
    date = models.DateTimeField(
        default=datetime.utcnow,
    )
    client_name = models.CharField(
        max_length=29,
    )
    email = models.EmailField(null=False, verbose_name='От кого(ваша почта)')
    message = models.TextField()


