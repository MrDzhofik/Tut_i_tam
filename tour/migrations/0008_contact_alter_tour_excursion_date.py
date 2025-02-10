# Generated by Django 5.1.2 on 2025-01-31 08:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0007_rename_text_tour_description_tour_hotel_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(max_length=100, verbose_name='Почта')),
                ('phone', models.CharField(max_length=50, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.AlterField(
            model_name='tour_excursion',
            name='date',
            field=models.DateField(default=datetime.date(2025, 1, 31)),
        ),
    ]
