from django.contrib import admin
from.models import Car

# admin.site.register(Car)
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["id_car", "model", "production_year"]
    list_filter = ["make", "production_year", "fuel", "date_ad"]
