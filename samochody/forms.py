from django.forms import ModelForm
from .models import Car

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["index", "id_car", "make", "model", "production_year", "price", "new_price", "mileage", "fuel", "capacity", "date_ad" ]

class SearchForm(ModelForm):
    class Meta:
        model = Car
        fields = ["index", "make", "model", "production_year", "price", "new_price", "mileage", "fuel", "capacity", "date_ad" ]