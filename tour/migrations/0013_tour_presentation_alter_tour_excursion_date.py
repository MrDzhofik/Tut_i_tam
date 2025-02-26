# Generated by Django 5.1.2 on 2025-02-20 12:19

import datetime
import tour.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0012_excursion_public_alter_tour_excursion_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='presentation',
            field=models.FileField(default='default.jpg', upload_to=tour.models.Tour.get_presentation_upload_path, verbose_name='Презентация'),
        ),
        migrations.AlterField(
            model_name='tour_excursion',
            name='date',
            field=models.DateField(default=datetime.date(2025, 2, 20)),
        ),
    ]
