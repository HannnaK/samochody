from django.urls import path
from .views import one_car, welcome, search

urlpatterns = [
    path('', welcome, name="powitanie"),
    path('wyszukiwanie/', search, name="wyszukiwanie"),
    path('szczegoly/<int:index>', one_car, name="dodatkowe_info"),
]
