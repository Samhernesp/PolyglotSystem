from django.views import View
from django.shortcuts import render, redirect
from .forms import OrderForm, OrderDetailForm
from .models import OrderDetail, Orders, Customer,Products
from .forms import ClientForm, ChildrenForm, ClientPlaceForm
from .mongo_models import Client, Children, ClientPlace
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from datetime import date

@method_decorator(login_required, name='dispatch')
class AddCoupleView(View):
    template_name = 'aditionalDataRegister.html'

    def get(self, request):
        current_user = request.user

        clients = Customer.objects.exclude(user=current_user)

        context = {
            'clients': clients,
        }

        return render(request, 'register_couple.html', context)
    
    def post(self,request):
        selected_client_id = request.POST.get('client_select')
        if selected_client_id is None:
            clients = Customer.objects.all()

            context = {
                'clients': clients,
            }
            return render(request, 'register_couple.html', context)
        else:
            customer = Customer.objects.filter(user=request.user).first()
            client = Client.objects(client_id=str(customer.customer_id)).first()
            client.couple_id = selected_client_id
            client.discount = True
            client.save()
            client_form = ClientForm()
            children_form = ChildrenForm()
            client_place_form = ClientPlaceForm()
            return render(request, self.template_name, {'client_form': client_form, 'children_form': children_form, 'client_place_form': client_place_form})

class LandingPageView(View):
    def get(self, request):
        return render(request, 'landing_page.html')
    


@method_decorator(login_required, name='dispatch')
class RegisterOrderView(View):
    form_class = OrderForm
    

    def get(self, request):
        form = self.form_class()
        return render(request, 'registerOrder.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            order = Orders()
            order.customer_id = form.cleaned_data['customer_id']
            order.order_date = form.cleaned_data['order_date']
            order.shipped_date = form.cleaned_data['shipped_date']
            order.payment_date = form.cleaned_data['payment_date']
            order.save(using='default')
            form = self.form_class()
            return render(request, 'registerOrder.html', {'form': form})
        
        print(form.errors)
        return render(request, 'registerOrder.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class OrderDetailView(View):
    form_class = OrderDetailForm


    def get(self, request):
        form = self.form_class()
        customer = Customer.objects.filter(user=request.user).first()
        orders = Orders.objects.filter(customer_id=customer.customer_id)
    
        return render(request, 'registerOrderDetail.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():

            customer = Customer.objects.filter(user=request.user).first()
    
            order = Orders()
            order.customer_id = customer
            order.order_date = date.today()
            order.shipped_date = date.today()
            order.payment_date = date.today()
            order.save(using='default')

            orderDetail = OrderDetail()
            orderDetail.order_number = order

            client = Client.objects(client_id=str(customer.customer_id)).first()
            
            orderDetail.product_id = form.cleaned_data['product_id']
            orderDetail.quantity = form.cleaned_data['quantity']

            product = Products.objects.filter(product_id=orderDetail.product_id.product_id).first()
            discount = 0

            if client:
                if client.discount:
                    price = float(product.selling_price) * int(orderDetail.quantity)

                    discount = float(product.selling_price) * 0.10
                    
                    orderDetail.price = price - discount
                else:
                    price = float(product.selling_price) * int(orderDetail.quantity)
                    orderDetail.price = price   
            else:       
                price = float(product.selling_price) * int(orderDetail.quantity)
                orderDetail.price = price   
            
            messages.success(request,f"Order added. Price ${orderDetail.price} Discount of ${discount}")

            orderDetail.save(using='default')
            
            return redirect('orderDetail')
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class ClientRegistrationView(View):
    template_name = 'aditionalDataRegister.html'

    def get(self, request):
        client_form = ClientForm()
        children_form = ChildrenForm()
        client_place_form = ClientPlaceForm()
        return render(request, self.template_name, {'client_form': client_form, 'children_form': children_form, 'client_place_form': client_place_form})

    def post(self, request):
        
        customer = Customer.objects.filter(user=request.user).first()
        client = Client.objects(client_id=str(customer.customer_id)).first()

        client_form = ClientForm(request.POST)
        client_place_form = ClientPlaceForm(request.POST)
        children_form = ChildrenForm(request.POST)

        if request.POST.get("form_type") == "form1":
            if client_form.is_valid():
                cleaned_data = client_form.cleaned_data

                # Hobbies
                hobbies = cleaned_data.get('hobbies')
                if hobbies:
                    client.hobbies = hobbies.split(',')
                    

                # Sports
                sports = cleaned_data.get('sports')
                if sports:
                    client.sports = sports.split(',')


                # Civil Status
                civil_status = cleaned_data.get('civil_status')
                if civil_status:
                    client.civil_status = civil_status


                # Civil Status Date
                civil_status_date = cleaned_data.get('civil_status_date')
                if civil_status_date:
                    client.civil_status_date = civil_status_date


                # Categories of Interest
                categories_of_interest = cleaned_data.get('categories_of_interest')
                if categories_of_interest:
                    client.categories_of_interest.append(categories_of_interest)

                # Guardar el objeto client
                client.discount = True
                client.save()
                client_form = ClientForm()

        if request.POST.get("form_type") == "form2":    
           
            if children_form.is_valid():
                cleaned_data = children_form.cleaned_data

                child = Children()  # Asumiendo que Children es una clase de modelo de documento

                # Name
                name = cleaned_data.get('name')
                if name:
                    child.name = name

                # Born Date
                born_date = cleaned_data.get('born_date')
                if born_date:
                    child.born_date = born_date

                # Genre
                genre = cleaned_data.get('genre')
                if genre:
                    child.genre = genre

                # Study
                # Nota: Como es un BooleanField con required=False, siempre tendrá un valor (True o False)
                child.study = cleaned_data.get('study', False)

                # Play Videogames
                # Nota: Igual que con 'study', siempre tendrá un valor booleano
                child.play_videogames = cleaned_data.get('play_videogames', False)

                # Videogames Platforms
                videogames_platforms = cleaned_data.get('videogames_platforms')

                if videogames_platforms:
                    # Suponiendo que se espera una lista. Ajusta según sea necesario
                    child.videogames_platforms = videogames_platforms.split(',')

                client.children.append(child)
                client.save()
                children_form = ChildrenForm()


        if request.POST.get("form_type") == "form3":    
            if client_place_form.is_valid():
                cleaned_data = client_place_form.cleaned_data

                client_place = ClientPlace()

                # City
                city = cleaned_data.get('city')
                if city:
                    client_place.city = city

                # State
                state = cleaned_data.get('state')
                if state:
                    client_place.state = state

                # Country
                country = cleaned_data.get('country')
                if country:
                    client_place.country = country

                # Postal Code
                postal_code = cleaned_data.get('postal_code')
                if postal_code:
                    client_place.postal_code = postal_code

                client.born_place = client_place
                client.save()
                client_place_form = ClientPlaceForm()


        if request.POST.get("form_type") == "form4":    
            if client_place_form.is_valid():
                cleaned_data = client_place_form.cleaned_data

                client_place = ClientPlace()

                # City
                city = cleaned_data.get('city')
                if city:
                    client_place.city = city

                # State
                state = cleaned_data.get('state')
                if state:
                    client_place.state = state

                # Country
                country = cleaned_data.get('country')
                if country:
                    client_place.country = country

                # Postal Code
                postal_code = cleaned_data.get('postal_code')
                if postal_code:
                    client_place.postal_code = postal_code

                client.place_residence = client_place
                client.save()
                client_place_form = ClientPlaceForm()



        return render(request, self.template_name, {'client_form': client_form, 'children_form': children_form, 'client_place_form': client_place_form})
