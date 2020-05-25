from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Car
from .forms import CarForm, SearchForm

# from rest_framework import generics
# from rest_framework.response import Response


def welcome(request):
    return render(request, 'home.html')


def all_cars(request):
    all = Car.objects.all().filter(is_activ=True)
    return render(request, 'cars.html', {'cars': all})


def one_car(request, index):
    car = get_object_or_404(Car, pk=index)

    form_car = CarForm(request.POST or None, request.FILES or None, instance=car)

    return render(request, 'car_form.html', {'form': form_car})

def is_valid_queryparam(param):
    return param != '' and param is not None

def search(request):
    all = Car.objects.all().filter(is_activ=True)
    make_set = set(Car.objects.values_list('make'))
    make_list=[]
    for _ in make_set:
        make_list.append(_[0])

    make_list_sort = sorted(make_list)



    id_car_contains_query = request.GET.get('id_car')
    make_contains_query = request.GET.get('make')
    year_min = request.GET.get('year_min')
    year_max = request.GET.get('year_max')
    date_ad_min = request.GET.get('date_ad_min')
    date_ad_max = request.GET.get('date_ad_max')

    if is_valid_queryparam(id_car_contains_query):
        all=all.filter(id_car__exact=id_car_contains_query)

    if is_valid_queryparam(make_contains_query) and make_contains_query != 'Wybierz markę':
        all=all.filter(make__icontains=make_contains_query)

    if is_valid_queryparam(year_min):
        all = all.filter(production_year__gte=year_min)

    if is_valid_queryparam(year_max):
        all = all.filter(production_year__lte=year_max)

    if is_valid_queryparam(date_ad_min):
        all = all.filter(date_ad__gte=date_ad_min)

    if is_valid_queryparam(date_ad_max):
        all = all.filter(date_ad__lte=date_ad_max)

    print(len(all))
    context = {
        'allcar': all,
        'make': make_list_sort
    }


    return render(request, 'search.html', context)

