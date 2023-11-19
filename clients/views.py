from django.views import View
from django.shortcuts import render, redirect
from .forms import OrderForm, OrderDetailForm
from .models import OrderDetail, Orders, Customer
from .forms import ClientForm, ChildrenForm, ClientPlaceForm
from .mongo_models import Client, Children, ClientPlace


class RegisterOrderView(View):
    form_class = OrderForm
    

    def get(self, request):
        # !!!!!!!!!!!!!!!!!!!
        # HEYEHEYEHYEHEY ESTA ES LA ID DEL CUSTOMEEEEEEER

        customer_id = self.request.GET.get("user")
        print(customer_id)
        # HEYEHEYEHYEHEY ESTA ES LA ID DEL CUSTOMEEEEEEER
        # !!!!!!!!!!!!!!!!!!!

        form = self.form_class()
        return render(request, 'registerOrder.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            order = Orders()
            order.product_id = form.cleaned_data['product_id']
            order.category_code = form.cleaned_data['category_code']
            order.description = form.cleaned_data['description']
            order.quantity_available = form.cleaned_data['quantity_available']
            order.cost = form.cleaned_data['cost']
            order.selling_price = form.cleaned_data['selling_price']
            order.save(using='default')

            return redirect('url_a_la_siguiente_vista')
        return render(request, self.template_name, {'form': form})

class OrderDetailView(View):
    form_class = OrderDetailForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'registerOrderDetail.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            orderDetail = OrderDetail()
            orderDetail.order_number = form.cleaned_data['order_number']
            orderDetail.product_id = form.cleaned_data['product_id']
            orderDetail.quantity = form.cleaned_data['quantity']
            orderDetail.price = form.cleaned_data['price']
            
            orderDetail.save(using='default')
            
            return redirect('url_a_la_siguiente_vista')
        return render(request, self.template_name, {'form': form})

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

        if request.POST.get("form_type") == "form1":
            client_form = ClientForm(request.POST)
            if client_form.is_valid():
                cleaned_data = client_form.cleaned_data

                # Hobbies
                hobbies = cleaned_data.get('hobbies')
                if hobbies:
                    client.hobbies.append(hobbies)

                # Sports
                sports = cleaned_data.get('sports')
                if sports:
                    client.sports.append(sports)

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
                client.save()


        children_form = ChildrenForm(request.POST)
        client_place_form = ClientPlaceForm(request.POST)
        if client_form.is_valid() and children_form.is_valid() and client_place_form.is_valid():
            
            return redirect('aditionalData')

        return render(request, self.template_name, {'client_form': client_form, 'children_form': children_form, 'client_place_form': client_place_form})
