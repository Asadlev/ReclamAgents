# Generated by Django 5.0.7 on 2024-07-17 05:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('client_name', models.CharField(max_length=29)),
                ('email', models.EmailField(max_length=254, verbose_name='От кого(ваша почта)')),
                ('message', models.TextField()),
            ],
        ),
    ]
