from django.views import View
from django.shortcuts import render, redirect
from .forms import ClienteDatosAdicionalesForm


class AditionalDataView(View):
    form_class = ClienteDatosAdicionalesForm


    def get(self, request):
        form = self.form_class()
        return render(request, 'aditionalDataRegister.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return redirect('url_a_la_siguiente_vista')
        return render(request, self.template_name, {'form': form})

class RegisterOrderView(View):
    form_class = OrderForm
    template_name = 'register-order.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_a_la_siguiente_vista')
        return render(request, self.template_name, {'form': form})

class OrderDetailView(View):
    form_class = OrderDetailForm
    template_name = 'register-order-detail.html'

    def get(self, request):
        form = self.form_class()
        return render(request, 'aditionalDataRegister.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_a_la_siguiente_vista')
        return render(request, self.template_name, {'form': form})

class RegisterOrderView(View):
    form_class = OrderForm
    template_name = 'register-order.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_a_la_siguiente_vista')
        return render(request, self.template_name, {'form': form})

class OrderDetailView(View):
    form_class = OrderDetailForm
    template_name = 'register-order-detail.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_a_la_siguiente_vista')
        return render(request, self.template_name, {'form': form})
