from django.http import HttpResponse
from django.db import models
from django.shortcuts import render, get_object_or_404
from .models import Cars
from .forms import CarForm


def welcome(request):
    return render(request, 'home.html')


def all_cars(request):
    all = Cars.objects.all().filter(is_activ=True)
    return render(request, 'cars.html', {'cars': all})


def one_car(request, index):
    car = get_object_or_404(Cars, pk=index)

    form_car = CarForm(request.POST or None, request.FILES or None, instance=car)

    return render(request, 'car_form.html', {'form': form_car})

def is_valid_queryparam(param):
    return param != '' and param is not None

def search(request):
    all = Cars.objects.all().filter(is_activ=True)
    make_set = set(Cars.objects.values_list('make'))
    make_list=[]
    for _ in make_set:
        make_list.append(_[0])

    fuel_set = set(Cars.objects.values_list('fuel'))
    fuel_list = []
    for _ in fuel_set:
        fuel_list.append(_[0])

    make_list_sort = sorted(make_list)
    fuel_list_sort = sorted(fuel_list)

    id_car_contains_query = request.GET.get('id_car')
    make_contains_query = request.GET.get('make')
    fuel_contains_query = request.GET.get('fuel')
    year_min = request.GET.get('year_min')
    year_max = request.GET.get('year_max')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    date_ad_min = request.GET.get('date_ad_min')
    date_ad_max = request.GET.get('date_ad_max')
    mileage_min = request.GET.get('mileage_min')
    mileage_max = request.GET.get('mileage_max')
    capacity_min = request.GET.get('capacity_min')
    capacity_max = request.GET.get('capacity_max')
    new_price = request.GET.get('new_price')


    if is_valid_queryparam(id_car_contains_query):
        all=all.filter(id_car__exact=id_car_contains_query)

    if is_valid_queryparam(make_contains_query) and make_contains_query != 'Wybierz markę':
        all=all.filter(make__icontains=make_contains_query)

    if is_valid_queryparam(fuel_contains_query) and fuel_contains_query != 'Wybierz paliwo':
        all = all.filter(fuel__exact=fuel_contains_query)

    if is_valid_queryparam(year_min):
        all = all.filter(production_year__gte=year_min)
    if is_valid_queryparam(year_max):
        all = all.filter(production_year__lte=year_max)

    if is_valid_queryparam(price_min):
        all = all.filter(price__gte=price_min)
    if is_valid_queryparam(price_max):
        all = all.filter(price__lte=price_max)

    if is_valid_queryparam(date_ad_min):
        all = all.filter(date_ad__gte=date_ad_min)
    if is_valid_queryparam(date_ad_max):
        all = all.filter(date_ad__lte=date_ad_max)

    if is_valid_queryparam(mileage_min):
        all = all.filter(mileage__gte=mileage_min)
    if is_valid_queryparam(mileage_max):
        all = all.filter(mileage__lte=mileage_max)

    if is_valid_queryparam(capacity_min):
        all = all.filter(capacity__gte=capacity_min)
    if is_valid_queryparam(capacity_max):
        all = all.filter(capacity__lte=capacity_max)

    if new_price == "on":
        all = all.exclude(new_price=0)
        all=all.filter(price__gt=models.F('new_price'))
    if new_price == "off":
        all = all.exclude(new_price=0)
        all = all.filter(price__lt=models.F('new_price'))


    print(len(all))


    context = {
        'allcar': all,
        'make': make_list_sort,
        'fuels': fuel_list_sort
    }


    return render(request, 'search.html', context)

