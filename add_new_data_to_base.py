import csv
import sqlite3
import pandas as pd
import math

makerlist = ['audi-a3', 'audi-a4', 'audi-a5', 'audi-a6', 'Honda', 'Hyundai', 'Toyota']
previous_data = '2021-01-03'
data = '2021-01-04'

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
    print('****')

except FileNotFoundError:
    pass

carlist = []

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
            car.append(data)

            if maker == 'audi-a3' or maker == 'audi-a4' or maker == 'audi-a5' or maker == 'audi-a6':
                car.append('Audi')
            else:
                car.append(maker)
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

            carlist.append(car)
print(carlist[0])

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

cars = pd.read_csv('otomoto/csv_files_with_data/allcars' + '-' + data + '.csv', header=None, encoding='utf-8')

cars.columns = ["price", "model", "id_car", "production_year", "mileage", "capacity", "fuel", "date_ad",
                'make', 'is_activ', 'new_price', 'currency']

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
guery = "DROP TABLE IF EXISTS 'cars'"

c.execute(guery)

cars.to_sql("cars", conn)

conn.commit()
conn.close()
