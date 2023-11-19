from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from clients.models import Customer 
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from clients.mongo_models import Client

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            user.save()

            customer = Customer()
            customer.user = user
            customer.first_name = form.cleaned_data['first_name']
            customer.last_name = form.cleaned_data['last_name']
            customer.address = form.cleaned_data['address']
            customer.date_of_birth = form.cleaned_data['date_of_birth']
            customer.email = form.cleaned_data['email']
            customer.home_phone = form.cleaned_data['home_phone']
            customer.cell_phone = form.cleaned_data['cell_phone']

            customer.save()

            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)   
                
                customer = Customer.objects.filter(user=request.user).first()
                print(customer)
                client = Client(client_id=str(customer.customer_id))
                client.save()

                return redirect('/registerOrder')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')