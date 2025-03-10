from django.db import models
import datetime
import os
from django.utils.text import slugify

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
    description = models.TextField(verbose_name="Описание", default="Тур")
    photo = models.ImageField(verbose_name="Фото", default="default.JPG", upload_to="tour_photo")
    hotel_description = models.TextField(verbose_name="Описание отелей", default="Отель")

    def get_presentation_upload_path(self, filename):
        return os.path.join('tour_presentation', self.name, filename)
    
    presentation = models.FileField(verbose_name="Презентация", default="default.jpg", upload_to=get_presentation_upload_path)

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
    photo = models.ImageField(verbose_name="Фото", default="default.JPG", upload_to="hotel")

    def get_hotel_upload_path(self, filename):
        return os.path.join('hotel', self.hotel.name, filename)
    
    photo = models.ImageField(verbose_name="Фото", default="default.JPG", upload_to=get_hotel_upload_path)

    class Meta:
       verbose_name = "Фото отеля"
       verbose_name_plural = "Фото отелей"
    
    def __str__(self):
        name = self.photo.url.split("/")[-1]
        return f"{self.hotel} - {name}"
    
class Excursion(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название экскурсии")
    interval = models.CharField(max_length=50, verbose_name="Продолжительность")
    description = models.TextField(verbose_name="Описание", default="Экскурсия")
    route = models.TextField(verbose_name="Маршрут", default="Маршрут")
    in_price = models.TextField(verbose_name="Входит в стоимость", default="Поездка")
    out_price = models.TextField(verbose_name="Не входит в стоимость", default="Личные расходы")
    price = models.TextField(verbose_name="Стоимость билета", default="Бесценно")
    public = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Экскурсия"
        verbose_name_plural = "Экскурсии"

    def __str__(self):
        return self.name
    
    def get_first_photo(self):
        first_photo = Excursion_photo.objects.filter(excursion=self).first()
        return first_photo.photo.url if first_photo else "default.JPG"
    
class Excursion_photo(models.Model):
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE, verbose_name="Отель")

    def get_excursion_upload_path(self, filename):
        return os.path.join('excursion', self.excursion.name, filename)
    
    photo = models.ImageField(verbose_name="Фото", default="default.JPG", upload_to=get_excursion_upload_path)
    

    class Meta:
       verbose_name = "Фото экскурсии"
       verbose_name_plural = "Фото экскурсии"
    
    def __str__(self):
        name = self.photo.url.split("/")[-1]
        return f"{self.excursion} - {name}"

class Tour_Excursion(models.Model):
    tour = models.ForeignKey(Tour, verbose_name="Тур", on_delete=models.CASCADE)
    excursion = models.ForeignKey(Excursion, verbose_name="Экскурсия", on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today())

    class Meta:
        verbose_name = "Тур_Экскурсия"
        verbose_name_plural = "Тур-Экскурсии"

    def __str__(self):
        return self.tour.name+ self.excursion.name

class Tour_Hotel(models.Model):
    tour = models.ForeignKey(Tour, verbose_name="Тур", on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, verbose_name="Отель", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Тур_Отель"
        verbose_name_plural = "Тур-Отели"

    def __str__(self):
        return self.tour.name  + " - " + self.hotel.name
    


class Contact(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя", blank=False)
    email = models.EmailField(max_length=100, verbose_name="Почта", blank=False)
    phone = models.CharField(max_length=50, verbose_name="Номер телефона", blank=False)
    message = models.CharField(max_length=500, verbose_name="Сообщение", blank=True)
    place = models.CharField(max_length=255, verbose_name="Место отправления", blank=True)
    date = models.DateField(verbose_name="Дата экскурсии", default=datetime.date.today)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"Заявка {self.user.username} на {self.excursion} ({self.date})"
