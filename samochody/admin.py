from django.contrib import admin
from.models import Cars

@admin.register(Cars)
class CarAdmin(admin.ModelAdmin):

    list_display = ["id_car", "model", "production_year"]
    list_filter = ["make", "production_year", "fuel", "date_ad"]
