# Generated by Django 5.1.2 on 2025-02-01 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0008_contact_alter_tour_excursion_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursion',
            name='in_price',
            field=models.TextField(default='Поездка', verbose_name='Входит в стоимость'),
        ),
        migrations.AddField(
            model_name='excursion',
            name='out_price',
            field=models.TextField(default='Личные расходы', verbose_name='Не входит в стоимость'),
        ),
        migrations.AddField(
            model_name='excursion',
            name='price',
            field=models.TextField(default='Бесценно', verbose_name='Стоимость билета'),
        ),
        migrations.AddField(
            model_name='excursion',
            name='route',
            field=models.TextField(default='Маршрут', verbose_name='Маршрут'),
        ),
        migrations.AlterField(
            model_name='tour_excursion',
            name='date',
            field=models.DateField(default=datetime.date(2025, 2, 1)),
        ),
    ]
