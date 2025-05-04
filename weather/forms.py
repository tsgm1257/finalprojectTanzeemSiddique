
from django import forms
from .models import ClothingRating

class LocationForm(forms.Form):
    location = forms.CharField(label='Enter your city', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'e.g. New York'
    }))

class RatingForm(forms.ModelForm):
    class Meta:
        model = ClothingRating
        fields = ['rating', 'feedback']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optional feedback'}),
        }
