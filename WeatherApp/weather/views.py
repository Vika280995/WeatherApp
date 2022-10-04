from django.shortcuts import render
import requests


def index(request):
    appid = "eed4d308bb2a4fa82123dc31313745a7"
    url ="https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+appid
    city = 'Minsk'
    res = requests.get(url.format(city))
    print(res.text)
    return render (request,'weather/index.html')
