from django.db import models
import datetime

# Create your models here.

class Town(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name

class Tour(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название тура")
    start_date = models.DateField(default=datetime.date.today, verbose_name="Дата начала")
    end_date = models.DateField(default=datetime.date.today, verbose_name="Дата конца")
    town = models.ForeignKey(Town, on_delete=models.CASCADE, related_name='towns', verbose_name="Город")
    price = models.IntegerField(verbose_name="Цена тура")
    text = models.TextField(verbose_name="Описание", default="Тур")
    photo = models.ImageField(verbose_name="Фото", default="default.JPG", upload_to="tour_photo") # add upload_to

    class Meta:
       verbose_name = "Тур"
       verbose_name_plural = "Туры"

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    info = models.TextField(verbose_name="Описание")

    class Meta:
       verbose_name = "Отель"
       verbose_name_plural = "Отели"

    def __str__(self):
        return self.name

class Hotel_photo(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name="Отель")
    image_url = models.FilePathField(verbose_name="Путь до картинки")


class Tour_Info(models.Model):
    tour = models.OneToOneField(Tour, verbose_name="Тур", on_delete=models.CASCADE)
    # excursion = models.
    # hotel = models.
