from .models import Tiny
from django.forms import ModelForm, TextInput

class TinyForm(ModelForm):
    class Meta:
        model = Tiny
        fields = ['full_url']

        widgets = {
            "full_url": TextInput(attrs={'class': 'form-control', 'placeholder': 'Вставить url'}),
        }