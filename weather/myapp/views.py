from django.shortcuts import render,redirect
import requests
from django.contrib import messages

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=e1c840578bd5e94376bf0df3c969b46c'
    city = 'Ahmedabad'
    if request.method=='POST':
        city = request.POST.get('city')

    rag = requests.get(url.format(city)).json()
    
    if rag['cod']!="404":    
        context = {
            'city' : city,
            'temp' : round(int(rag['main']['temp'])-273.15),
            'description':rag['weather'][0]['description'],
            'icon' : rag['weather'][0]['icon'],
        }
        return render(request,'weather.html',context)
    else:
        messages.error(request,"City Not found")
        return render(request,'weather.html')
        
    