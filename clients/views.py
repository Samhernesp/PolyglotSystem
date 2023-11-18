from django.views import View
from django.shortcuts import render, redirect
from .forms import ClienteDatosAdicionalesForm
from .models import Pedido  

class RegistroDatosAdicionalesView(View):
    form_class = ClienteDatosAdicionalesForm
    template_name = 'registro_datos_adicionales.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return redirect('url_a_la_siguiente_vista')
        return render(request, self.template_name, {'form': form})
