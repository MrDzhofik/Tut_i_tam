# Generated by Django 5.1.2 on 2025-02-04 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0009_excursion_in_price_excursion_out_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.CharField(blank=True, max_length=500, verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='tour_excursion',
            name='date',
            field=models.DateField(default=datetime.date(2025, 2, 4)),
        ),
    ]
