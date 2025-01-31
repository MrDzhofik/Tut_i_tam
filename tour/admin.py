from django.contrib import admin
from .models import Town, Tour, Hotel, Hotel_photo, Excursion, Excursion_photo, Tour_Excursion, Tour_Hotel, Contact

# Register your models here.

admin.site.register(Town)
admin.site.register(Tour)
admin.site.register(Hotel)
admin.site.register(Hotel_photo)
admin.site.register(Tour_Hotel)

admin.site.register(Excursion)
admin.site.register(Excursion_photo)
admin.site.register(Tour_Excursion)

admin.site.register(Contact)

