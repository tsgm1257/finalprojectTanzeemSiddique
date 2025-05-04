import requests
import urllib.parse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import LocationForm, RatingForm
from .models import WeatherPreference, ClothingRating
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

def login_register(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            register_form = UserCreationForm()
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('home')
        elif 'register' in request.POST:
            register_form = UserCreationForm(request.POST)
            login_form = AuthenticationForm()
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect('home')
    else:
        login_form = AuthenticationForm()
        register_form = UserCreationForm()

    return render(request, 'weather/login_register.html', {
        'login_form': login_form,
        'register_form': register_form
    })


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
                url = f"https://open-weather13.p.rapidapi.com/city/{encoded_location}/EN"
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
    pref_id = request.GET.get('pref_id') or request.POST.get('pref_id')

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.preference_id = pref_id
            rating.save()
            return render(request, 'weather/rate.html', {
                'form': RatingForm(),
                'show_modal': True
            })
    else:
        form = RatingForm()

    return render(request, 'weather/rate.html', {
        'form': form,
        'pref_id': pref_id
    })

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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'weather/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'weather/register.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return redirect('home')

@login_required
def my_ratings(request):
    ratings = ClothingRating.objects.filter(user=request.user).select_related('preference')
    return render(request, 'weather/my_ratings.html', {'ratings': ratings})