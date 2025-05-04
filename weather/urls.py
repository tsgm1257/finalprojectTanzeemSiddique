from django.contrib import admin
from django.urls import path
from weather import views as weather_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', weather_views.home, name='home'),
    path('about/', weather_views.about, name='about'),
    path('result/', weather_views.result, name='result'),
    path('rate/', weather_views.rate, name='rate'),
    path('login_register/', weather_views.login_register, name='login_register'),
    path('login/', weather_views.login_view, name='login'),
    path('register/', weather_views.register_view, name='register'),
    path('logout/', weather_views.logout_view, name='logout'),
    path('myratings/', weather_views.my_ratings, name='my_ratings'),  # step 4
]
