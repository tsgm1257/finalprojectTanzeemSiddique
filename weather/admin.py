
from django.contrib import admin
from .models import WeatherPreference, ClothingRating

@admin.register(WeatherPreference)
class WeatherPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'temperature', 'condition', 'recommendation', 'timestamp')
    search_fields = ('location', 'user__username')

@admin.register(ClothingRating)
class ClothingRatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'preference', 'rating', 'feedback')
    search_fields = ('user__username',)
