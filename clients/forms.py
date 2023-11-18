from django import forms
from .models import Orders, OrderDetail

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['customer_id', 'order_date', 'shipped_date', 'payment_date']

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['order_number', 'product_id', 'quantity', 'price']

class ChildrenForm(forms.Form):
    name = forms.CharField(required=True)
    born_date = forms.DateTimeField(required=False)
    genre = forms.CharField(required=False)
    study = forms.BooleanField(required=False, initial=False)
    play_videogames = forms.BooleanField(required=False, initial=False)
    videogames_platforms = forms.MultipleChoiceField(choices=[], required=False)  # Actualiza las opciones según sea necesario

class ClientPlaceForm(forms.Form):
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    country = forms.CharField(required=False)
    postal_code = forms.CharField(required=False)

class ClientForm(forms.Form):
    client_id = forms.CharField(required=True)
    born_place = forms.CharField(required=False)  # Manejo como campo de texto simple, ajusta según sea necesario
    place_residence = forms.CharField(required=False)  # Manejo como campo de texto simple, ajusta según sea necesario
    hobbies = forms.MultipleChoiceField(choices=[], required=False)  # Actualiza las opciones según sea necesario
    civil_status = forms.CharField(required=False)
    civil_status_date = forms.DateTimeField(required=False)
    couple = forms.CharField(required=False)  # Ajusta según sea necesario
    categories_of_interest = forms.MultipleChoiceField(choices=[], required=False)  # Actualiza las opciones según sea necesario

