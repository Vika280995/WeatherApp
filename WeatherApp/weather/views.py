from django.shortcuts import render
import requests
from .models import City
from.forms import CityForm



def index(request):
    appid = "eed4d308bb2a4fa82123dc31313745a7"
    url ="https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}"

    if(request.method=='POST'):
        form=CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities =[]

    for city in cities:
        res = requests.get(url.format(city.name,appid)).json()
        if res['cod']==200 and city.name not in (c['city'] for c in all_cities):
            city_info = {
                'city': city.name,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon']
        }
    all_cities.append(city_info)


    context={'all_info':all_cities,'form':form}
    return render (request,'weather/index.html',context)
