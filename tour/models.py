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
    photo = models.ImageField(verbose_name="Фото", default="default.JPG", upload_to="tour_photo")

    class Meta:
       verbose_name = "Тур"
       verbose_name_plural = "Туры"

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    info = models.TextField(verbose_name="Описание")
    adress = models.CharField(max_length=100, verbose_name="Адрес", default="Гагра")

    class Meta:
       verbose_name = "Отель"
       verbose_name_plural = "Отели"

    def __str__(self):
        return self.name

class Hotel_photo(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name="Отель")
    image_url = models.CharField(max_length=100, verbose_name="Путь до картинки", default="")

    class Meta:
       verbose_name = "Фото отеля"
       verbose_name_plural = "Фото отелей"
    
    def __str__(self):
        return self.hotel + self.image_url

class Excursion(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название экскурсии")
    interval = models.CharField(max_length=50, verbose_name="Продолжительность")
    description = models.TextField(verbose_name="Описание", default="Экскурсия")

    class Meta:
        verbose_name = "Экскурсия"
        verbose_name_plural = "Экскурсии"

    def __str__(self):
        return self.name
    
class Excursion_photo(models.Model):
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE, verbose_name="Отель")
    image_url = models.CharField(max_length=100, verbose_name="Путь до картинки", default="")

    class Meta:
       verbose_name = "Фото экскурсии"
       verbose_name_plural = "Фото экскурсии"
    
    def __str__(self):
        return self.excursion + self.image_url

class Tour_Excursion(models.Model):
    tour = models.ForeignKey(Tour, verbose_name="Тур", on_delete=models.CASCADE)
    excursion = models.ForeignKey(Excursion, verbose_name="Экскурсия", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Тур_Экскурсия"
        verbose_name_plural = "Тур-Экскурсии"

    def __str__(self):
        return self.tour + self.excursion

class Tour_Hotel(models.Model):
    tour = models.ForeignKey(Tour, verbose_name="Тур", on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, verbose_name="Отель", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Тур_Отель"
        verbose_name_plural = "Тур-Отели"

    def __str__(self):
        return self.tour + self.hotel
