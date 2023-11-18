from django import forms
from .models import CustomerAditionalData, Orders, OrderDetail

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
            'children':forms.Select(attrs={'class': 'form-control mb-3', 'placeholder': 'Hijos:'}),
            'birth_place':forms.Select(attrs={'type': 'date','class': 'form-control', 'placeholder': 'Fecha nacimiento:'}),
            'place_location':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Lugar Vivienda:'}),
            'hobbies':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Hijos:'}),
            'sports':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Lugar nacimiento:'}),
            'civil_status':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Lugar Vivienda:'}),
            'interest_categories':forms.Select(attrs={'class': 'form-control mb-3', 'placeholder': 'Hijos:'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['customer_id', 'order_date', 'shipped_date', 'payment_date']

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['order_number', 'product_id', 'quantity', 'price']