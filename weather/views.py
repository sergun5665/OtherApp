import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
import pathlib
from bs4 import BeautifulSoup



def index(request):
    appid = '6a532c3f4f38d85200410088f8d83821'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)
    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)

def certificates(request):
    return render(request, 'weather/certificates.html')



def news(request):
    BASE_URL = 'https://news.google.com/?tab=rn&hl=ru&gl=RU&ceid=RU:ru'  # 1,2
    BASE_SAVE_PATH = pathlib.Path('./weather/templates/weather')  # 1

    r = requests.get(BASE_URL)  # 1,2

    html_file_path = BASE_SAVE_PATH / 'news.html'  # 1

    with open(str(html_file_path.absolute()), 'wb') as f:  # 1
        f.write(r.content)  # 1
    soap = BeautifulSoup(r.text, "html.parser")  # 2
    print(soap.title)  # 2

    return render(request, 'weather/news.html')

