import requests
import urllib.parse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import LocationForm, RatingForm
from .models import WeatherPreference, ClothingRating

RAPIDAPI_KEY = '18bbf37254msh86222c1227b8dbfp1ebc20jsn2e17a62895fb'

def recommend_clothing(temp, condition):
    if 'rain' in condition.lower():
        return "Wear a raincoat and waterproof shoes."
    elif temp < 10:
        return "Wear a warm jacket and a scarf."
    elif temp < 20:
        return "Wear a sweater or hoodie."
    else:
        return "Light clothing is fine for the weather."

def home(request):
    form = LocationForm()
    return render(request, 'weather/home.html', {'form': form})

def result(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            try:
                # URL-encode the location to handle spaces and special characters
                encoded_location = urllib.parse.quote(location)
                url = "https://open-weather13.p.rapidapi.com/city/Dallas/EN"
                headers = {
                    "X-RapidAPI-Key": RAPIDAPI_KEY,
                    "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
                }
                res = requests.get(url, headers=headers)
                data = res.json()
                print("STATUS CODE:", res.status_code)
                print("RESPONSE JSON:", data)

                if res.status_code != 200 or 'main' not in data:
                    raise ValueError("API error")

                temp = data['main']['temp']
                condition = data['weather'][0]['description']
                recommendation = recommend_clothing(temp, condition)

                preference = WeatherPreference.objects.create(
                    user=request.user,
                    location=location,
                    temperature=temp,
                    condition=condition,
                    recommendation=recommendation
                )

                return render(request, 'weather/result.html', {
                    'location': location,
                    'temp': temp,
                    'condition': condition,
                    'recommendation': recommendation,
                    'pref_id': preference.id
                })
            except Exception as e:
                print("ERROR:", e)
                return render(request, 'weather/result.html', {'error': 'Unable to fetch weather. Try again.'})
    return redirect('home')

def rate(request):
    if request.method == 'POST':
        pref_id = request.POST.get('pref_id')
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.preference_id = pref_id
            rating.save()
            return redirect('home')
    return render(request, 'weather/rate.html', {'form': RatingForm()})

def about(request):
    return render(request, 'weather/about.html')

def login_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'weather/login_register.html', {'form': form})
