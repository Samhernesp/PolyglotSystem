from django.views import View
from django.shortcuts import render, redirect
from .forms import ClienteDatosAdicionalesForm
from .models import CustomerAditionalData, Pedido  

class RegistroDatosAdicionalesView(View):
    form_class = ClienteDatosAdicionalesForm
    template_name = 'registro_datos_adicionales.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = CustomerAditionalData()
            data.children = form.cleaned_data['children']
            data.birth_place = form.cleaned_data['birth_place']
            data.place_location = form.cleaned_data['place_location']
            data.hobbies = form.cleaned_data['hobbies']
            data.sports = form.cleaned_data['sports']
            data.civil_status = form.cleaned_data['civil_status']
            data.interest_categories = form.cleaned_data['interest_categories']
            data.save(using='cosacoasasod')
            return redirect('url_a_la_siguiente_vista')
        return render(request, self.template_name, {'form': form})
