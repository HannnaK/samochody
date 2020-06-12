from django.forms import ModelForm
from .models import Cars

class CarForm(ModelForm):
    class Meta:
        model = Cars
        fields = ["id_car", "make", "model", "production_year", "price", "currency", "new_price", "mileage", "fuel", "capacity", "date_ad" ]
