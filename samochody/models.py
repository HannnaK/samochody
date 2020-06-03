from django.db import models


class Cars(models.Model):
    index = models.PositiveIntegerField(blank=True, primary_key=True)
    price = models.IntegerField("cena", blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    id_car = models.BigIntegerField("ID samochodu", blank=True, null=True)
    production_year = models.PositiveSmallIntegerField("rok produkcji", blank=True, null=True)
    mileage = models.IntegerField("przebieg", blank=True, null=True)
    capacity = models.IntegerField("pojemność", blank=True, null=True)
    fuel = models.CharField("rodzaj paliwa", max_length=20, blank=True, null=True)
    date_ad = models.CharField("data dodania", max_length=20, blank=True, null=True)
    make = models.CharField("marka", max_length=20, blank=True, null=True)
    is_activ = models.BooleanField(blank=True, null=True)
    new_price = models.PositiveIntegerField("nowa cena", blank=True, null=True)

    def __str__(self):
        return '{id_car}__{price}'.format(id_car=self.id_car, price=self.price, new_price=self.new_price )

    class Meta:
        managed = False
        db_table = 'cars'
