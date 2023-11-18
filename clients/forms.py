from django import forms
from .models import CustomerAditionalData

class ClienteDatosAdicionalesForm(forms.ModelForm):
    class Meta:
        model = CustomerAditionalData
        fields = [
            'children',
            'birth_place',
            'place_location',
            'hobbies',
            'sports',
            'civil_status',
            'interest_categories',
        ]
        widgets = {
            'children':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Hijos:'}),
            'birth_place':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Lugar nacimiento:'}),
            'place_location':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Lugar Vivienda:'}),
        }