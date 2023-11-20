from django import forms
from .models import Orders, OrderDetail, CategoryProducts

inputStyle = 'focus:outline-none block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"'
class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['customer_id', 'order_date', 'shipped_date', 'payment_date']

    def __init__(self, *args, **kwargs):
            super(OrderForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = inputStyle
                
class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['product_id', 'quantity']

    def __init__(self, *args, **kwargs):
            super(OrderDetailForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():


                visible.field.widget.attrs['class'] = inputStyle

class ChildrenForm(forms.Form):
    name = forms.CharField(required=False)
    born_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    genre = forms.ChoiceField(
        choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')],
        required=False
    )
    study = forms.BooleanField(required=False, initial=False)
    play_videogames = forms.BooleanField(required=False, initial=False)
    videogames_platforms = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(ChildrenForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name not in ['study', 'play_videogames']:
                visible.field.widget.attrs['class'] = inputStyle

class ClientPlaceForm(forms.Form):
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    country = forms.CharField(required=False)
    postal_code = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(ClientPlaceForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = inputStyle

class ClientForm(forms.Form):
    hobbies = forms.CharField(required=False)  
    sports = forms.CharField(required=False)
    civil_status = forms.CharField(required=False)
    civil_status_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    categories_of_interest = forms.MultipleChoiceField(
            choices=[(category.description, category.description) for category in CategoryProducts.objects.all()],
            widget=forms.CheckboxSelectMultiple(),
            required=False
    )

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if not visible.name == 'categories_of_interest':
                visible.field.widget.attrs['class'] = inputStyle
