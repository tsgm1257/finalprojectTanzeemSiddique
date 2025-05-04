
from django.db import models
from django.contrib.auth.models import User

class WeatherPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    condition = models.CharField(max_length=100)
    recommendation = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} - {self.recommendation[:20]}..."

class ClothingRating(models.Model):
    preference = models.ForeignKey(WeatherPreference, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"Rating {self.rating} by {self.user.username}"
