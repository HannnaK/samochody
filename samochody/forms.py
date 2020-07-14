from django.forms import ModelForm
from .models import Cars, Models, Fuels


class CarForm(ModelForm):
    class Meta:
        model = Cars
        fields = ( "id_car", "production_year", "price", "date_ad", "mileage", "capacity", "new_price")

class ModelForm(ModelForm):
    class Meta:
        model = Models
        fields = ["model"]

class FuelForm(ModelForm):
    class Meta:
        model = Fuels
        fields = ["fuel"]