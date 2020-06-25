from django.contrib import admin
from.models import Cars

# admin.site.register(Car)
@admin.register(Cars)
class CarAdmin(admin.ModelAdmin):
    list_display = ["id_car", "id_model", "production_year"]
    list_filter = [ "production_year", "id_fuel", "date_ad"]
