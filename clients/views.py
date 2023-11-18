from django.views import View
from django.shortcuts import render, redirect
from .forms import OrderForm, OrderDetailForm
from .models import OrderDetail, Orders
from .forms import ClientForm, ChildrenForm, ClientPlaceForm
from .mongo_models import Client, Children, ClientPlace


class RegisterOrderView(View):
    form_class = OrderForm
    

    def get(self, request):
        # !!!!!!!!!!!!!!!!!!!
        # HEYEHEYEHYEHEY ESTA ES LA ID DEL CUSTOMEEEEEEER

        customer_id = self.request.GET.get("user")
        
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
        client_form = ClientForm(request.POST)
        children_form = ChildrenForm(request.POST)
        client_place_form = ClientPlaceForm(request.POST)
        client = Client()
        client = Client(client_id='4848')
        client.save()
        if client_form.is_valid() and children_form.is_valid() and client_place_form.is_valid():
            
            return redirect('some-success-url')

        return render(request, self.template_name, {'client_form': client_form, 'children_form': children_form, 'client_place_form': client_place_form})
