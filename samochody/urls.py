from django.urls import path
from .views import all_cars, one_car, welcome, search

urlpatterns = [
    path('', welcome, name="powitanie"),
    path('wszystkie/', all_cars, name="wszystkie_samochody"),
    path('wyszukiwanie/', search, name="wyszukiwanie"),
    path('szczegoly/<int:index>', one_car, name="dodatkowe_info"),

]