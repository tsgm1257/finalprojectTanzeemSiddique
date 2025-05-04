
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
    path('rate/', views.rate, name='rate'),
    path('about/', views.about, name='about'),
    path('login_register/', views.login_register, name='login_register'),
]
