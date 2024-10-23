# Generated by Django 5.1.2 on 2024-10-22 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0004_excursion_alter_hotel_photo_options_hotel_adress_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excursion_photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(default='', max_length=100, verbose_name='Путь до картинки')),
                ('excursion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.excursion', verbose_name='Отель')),
            ],
            options={
                'verbose_name': 'Фото экскурсии',
                'verbose_name_plural': 'Фото экскурсии',
            },
        ),
    ]
