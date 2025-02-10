from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name="home"),
    path('tour/<int:tour_id>/', views.show_tour, name="tour_info"),
    path('excursion/<int:excursion_id>', views.show_excursion, name="excursion_info"),
    path('hotel/<int:hotel_id>', views.show_hotel, name="hotel_info"),
    path('excursion_order/<int:excursion_id>', views.excursion_order_show, name="excursion_order"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
