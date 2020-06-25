import csv
import sqlite3
import pandas as pd
import math

makerlist = ['audi-a3', 'audi-a4', 'audi-a5', 'audi-a6', 'Honda', 'Hyundai', 'Toyota']
previous_data = '2020-06-12'
data = '2020-06-19'

old_carlist = []
try:
    fileName = 'otomoto/csv_files_with_data/allcars' + '-' + previous_data + '.csv'

    with open(fileName, 'r', newline='', encoding='utf-8') as cars:
        carreader = csv.reader(cars, delimiter=',')
        for car in carreader:
            car[0] = float(car[0])
            car[0] = math.floor(car[0])
            car[0] = int(car[0])
            try:
                car[4] = int(car[4])
            except ValueError:
                car[4] = None
            old_carlist.append(car)
    print(old_carlist[0])
    print(type(old_carlist[0][0]))

except FileNotFoundError:
    pass

carlist = []
model_car = set()
make_car = set()
fuel_car = set()
for maker in makerlist:
    fileName = 'otomoto/csv_files/' + maker + '-' + data + '.csv'

    with open(fileName, 'r') as cars:
        carreader = csv.reader(cars, delimiter=',')
        for car in carreader:

            car[1] = car[1].split(' ')

            try:
                for model in car[1]:
                    del car[1][2]
            except IndexError:
                pass
            car[1] = ' '.join(car[1])

            model_car.add(car[1])

            car.append(data)

            if maker == 'audi-a3' or maker == 'audi-a4' or maker == 'audi-a5' or maker == 'audi-a6':
                car.append('Audi')
                make_car.add('Audi')
            else:
                car.append(maker)
                make_car.add(maker)
            car.append(True)
            car.append(None)
            car[4] = car[4].replace('km', '').replace(' ', '')
            try:
                car[4] = int(car[4])
            except ValueError:
                car[4] = None
            car[5] = car[5].replace('cm3', '').replace(' ', '')

            car[0] = car[0].split('\n')
            car.append(car[0][1])
            car[0] = car[0][0]
            car[0] = car[0].replace(',', '.')
            car[0] = float(car[0])
            car[0] = math.floor(car[0])
            car[0] = int(car[0])

            fuel_car.add(car[6])

            carlist.append(car)
print(carlist[0])
print(type(carlist[0][0]))

model_car_sort = sorted(model_car)
make_car_sort = sorted(make_car)
fuel_car_sort = sorted(fuel_car)

model_car_dict = {model_car_sort[i]: i for i in range(0, len(model_car_sort))}
print('model_car_dict', model_car_dict)

make_car_dict = {make_car_sort[i]: i for i in range(0, len(make_car_sort))}
print('make_car_dict', make_car_dict)

fuel_car_dict = {fuel_car_sort[i]: i for i in range(0, len(fuel_car_sort))}
print('fuel_car_dict', fuel_car_dict)

for car in carlist:
    car[1] = model_car_dict[car[1]]

for car in carlist:
    car[8] = make_car_dict[car[8]]

for car in carlist:
    car[6] = fuel_car_dict[car[6]]

print(carlist[0], carlist[15000])

id_new_carlist = []
for car in carlist:
    id_new_carlist.append(car[2])

for old_car in old_carlist:
    if old_car[2] not in id_new_carlist:
        old_car[9] = False
    else:
        old_car[9] = True

    for new_car in carlist:
        if new_car[2] == old_car[2]:
            if new_car[0] == old_car[0]:
                carlist.remove(new_car)
            else:
                old_car[10] = new_car[0]
                carlist.remove(new_car)

for car in carlist:
    old_carlist.append(car)

print('*************')

current_database = 'otomoto/csv_files_with_data/allcars' + '-' + data + '.csv'
with open(current_database, 'w', encoding='utf-8', newline='') as cars:
    carwriter = csv.writer(cars)
    for car in old_carlist:
        carwriter.writerow(car)

current_database = 'otomoto/csv_files_with_data/allmakes' + '-' + data + '.csv'
with open(current_database, 'w', encoding='utf-8', newline='') as makes:
    makewriter = csv.writer(makes)
    for make in make_car_sort:
        makewriter.writerow([make])

current_database = 'otomoto/csv_files_with_data/allmodels' + '-' + data + '.csv'
with open(current_database, 'w', encoding='utf-8', newline='') as models:
    modelwriter = csv.writer(models)
    for model in model_car_sort:
        modelwriter.writerow([model])

current_database = 'otomoto/csv_files_with_data/allfuels' + '-' + data + '.csv'
with open(current_database, 'w', encoding='utf-8', newline='') as fuels:
    fuelwriter = csv.writer(fuels)
    for fuel in fuel_car_sort:
        fuelwriter.writerow([fuel])

cars = pd.read_csv('otomoto/csv_files_with_data/allcars' + '-' + data + '.csv', header=None, encoding='utf-8')

cars.columns = ["price", "id_model", "id_car", "production_year", "mileage", "capacity", "id_fuel", "date_ad",
                'id_make',
                'is_activ', 'new_price', 'currency']

makes = pd.read_csv('otomoto/csv_files_with_data/allmakes' + '-' + data + '.csv', header=None, encoding='utf-8')
makes.columns = ["make"]

models = pd.read_csv('otomoto/csv_files_with_data/allmodels' + '-' + data + '.csv', header=None, encoding='utf-8')
models.columns = ["model"]

fuels = pd.read_csv('otomoto/csv_files_with_data/allfuels' + '-' + data + '.csv', header=None, encoding='utf-8')
fuels.columns = ["fuel"]

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

guery = "DROP TABLE IF EXISTS 'cars'"
guery2 = "DROP TABLE IF EXISTS 'makes'"
guery3 = "DROP TABLE IF EXISTS 'models'"
guery4 = "DROP TABLE IF EXISTS 'fuels'"
c.execute(guery)
c.execute(guery2)
c.execute(guery3)
c.execute(guery4)

cars.to_sql("cars", conn)
makes.to_sql("makes", conn)
models.to_sql("models", conn)
fuels.to_sql("fuels", conn)
conn.commit()
conn.close()
