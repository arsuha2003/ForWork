from .models import Sites
from django.forms import ModelForm, TextInput

class SitesForm(ModelForm):
    class Meta:
        model = Sites
        fields = ['long_u']

        widgets = {
            "long_u": TextInput(attrs={'class': 'form-control', 'placeholder': 'Вставить url'}),
        }