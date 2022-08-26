from pydoc import describe
from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method=='POST':
        city = request.POST['city'].capitalize()
        res=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=a031a7adf8458c0a79fa637b954a5f8d').read()
        json_data=json.loads(res)
        whether_data={
            "country_code":str(json_data['sys']['country']),
            "coordinate":str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
            "temp":str(json_data['main']['temp'])+'k',
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
            "desc":str(json_data['weather'][0]['description']).capitalize(),
            "icon":str(json_data['weather'][0]['icon']),
        }

        return render (request,'index.html',{'city':city,'data':whether_data})
    return render(request,'index.html')