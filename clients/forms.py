from django import forms
from .models import CustomerAditionalData, Orders, OrderDetail, Children, BirthPlace, PlaceLocation, CivilStatus
from django.forms import inlineformset_factory

class ChildrenForm(forms.ModelForm):
    class Meta:
        model = Children
        fields = ['name', 'birth_date', 'genre', 'study', 'play_videogames','videogames_platform']

class BirthPlaceForm(forms.ModelForm):
    class Meta:
        model = BirthPlace
        fields = ['city', 'region', 'country']

class PlaceLocationForm(forms.ModelForm):
    class Meta:
        model = PlaceLocation
        fields = ['city', 'region', 'country', 'postal_code']

class CivilStatusForm(forms.ModelForm):
    class Meta:
        model = CivilStatus
        fields = ['status_type', 'date']

ChildrenFormset = inlineformset_factory(
    Children, CustomerAditionalData, 
    form=ChildrenForm, 
    extra=1,
    can_delete=True
)

class ClienteDatosAdicionalesForm(forms.ModelForm):
    class Meta:
        model = CustomerAditionalData
        fields = [
            'customer',
            'hobbies',
            'sports',
            'interest_categories'
        ]
        widgets = {
            'customer':forms.Select(attrs={'class': ''}),
            'hobbies':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Hobbies:'}),
            'sports':forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Deportes:'}),
            'interest_categories':forms.Select(attrs={'class': ''})
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['customer_id', 'order_date', 'shipped_date', 'payment_date']

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['order_number', 'product_id', 'quantity', 'price']