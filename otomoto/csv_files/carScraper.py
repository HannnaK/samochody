import requests, bs4, sys, csv, datetime

now = datetime.datetime.now()

makerlist = ['audi/a3', 'audi/a4', 'audi/a5', 'audi/a6', 'honda', 'hyundai', 'toyota']

for maker in makerlist:

    path = 'https://www.otomoto.pl/osobowe/uzywane/' + maker + '/od-2006'
    maker = maker.replace('/','-')
    print (maker)
    fileName = maker + '-' + str(now.date()) + '.csv'

    carFile = open(fileName, 'w', newline="")
    outputWriter = csv.writer(carFile)

    res = requests.get(path)
    res.raise_for_status()

    carSoup = bs4.BeautifulSoup(res.text, features="lxml")
    try:
        lastPage = int(carSoup.select('.page')[-1].text)
    except IndexError:
        lastPage = 1

    for i in range(1, lastPage + 1):
        print(i)
        res = requests.get(path + '?page=' + str(i))
        res.raise_for_status()
        currentPage = bs4.BeautifulSoup(res.text, features='lxml')

        carList = currentPage.select('article.offer-item')

        for car in carList:
            currentCarData = []
            price = car.find('span', class_='offer-price__number').text.strip().replace(" ", "")
            currentCarData.append(price)
            title = car.find('a', class_='offer-title__link').text.strip()
            currentCarData.append(title)
            id_car = car['data-ad-id']
            currentCarData.append(id_car)

            paramList = ["year", "mileage", "engine_capacity", "fuel_type"]
            for param in paramList:
                currentParameter = car.find('li', {"data-code": param})
                if (currentParameter):
                    currentCarData.append(currentParameter.text.strip())
                else:
                    currentCarData.append("")

            outputWriter.writerow(currentCarData)

    carFile.close()
