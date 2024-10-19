from django.contrib import admin
from .models import Town, Tour, Hotel, Hotel_photo

# Register your models here.

admin.site.register(Town)
admin.site.register(Tour)
admin.site.register(Hotel)
admin.site.register(Hotel_photo)
