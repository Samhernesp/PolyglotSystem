from django import forms 

inputStyle = {'class': 'focus:outline-none block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"'}
class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs=inputStyle))
    email = forms.EmailField(widget=forms.EmailInput(attrs=inputStyle))

    password = forms.CharField(widget=forms.PasswordInput(attrs=inputStyle))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs=inputStyle))

    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs=inputStyle))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs=inputStyle))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs=inputStyle))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs=inputStyle))
    home_phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs=inputStyle))
    cell_phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs=inputStyle))

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs=inputStyle))
    password = forms.CharField(widget=forms.PasswordInput(attrs=inputStyle))