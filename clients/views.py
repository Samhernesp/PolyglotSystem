from django.views import View
from django.shortcuts import render, redirect
from .forms import ClienteDatosAdicionalesForm, OrderForm, OrderDetailForm
from .models import CustomerAditionalData, BirthPlace, PlaceLocation, Children, CivilStatus, CategoryProducts


class AditionalDataView(View):
    model = ClienteDatosAdicionales
    form_class = ClienteDatosAdicionalesForm
    template_name = 'aditionalDataRegister.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['children_formset'] = ChildrenFormset(self.request.POST, instance=self.object)
            context['birth_place_form'] = BirthPlaceForm(self.request.POST)
            context['place_location_form'] = PlaceLocationForm(self.request.POST)
            context['civil_status_form'] = CivilStatus(self.request.POST)
        else:
            context['children_formset'] = ChildrenFormset()
            context['birth_place_form'] = BirthPlaceForm()
            context['place_location_form'] = PlaceLocationForm()
            context['civil_status_form'] = CivilStatus()
        return context

    def post(self, request):
        self.object = None
        form = self.get_form()
        children_formset = ChildrenFormset(self.request.POST)
        birth_place_form = BirthPlaceForm(self.request.POST)
        place_location_form = PlaceLocationForm(self.request.POST)
        civil_status_form = CivilStatus(self.request.POST)

        if (form.is_valid() and children_formset.is_valid() and 
            birth_place_form.is_valid() and place_location_form.is_valid() and civil_status_form.is_valid()):
            return self.form_valid(form, children_formset, birth_place_form, place_location_form,civil_status_form)
        else:
            return self.form_invalid(form, children_formset, birth_place_form, place_location_form,civil_status_form)

    def form_valid(self, form, children_formset, birth_place_form, place_location_form,civil_status_form):
        self.object = form.save()

        BirthPlace = BirthPlace()
        BirthPlace = birth_place_form.save(commit=False)
        BirthPlace.save()

        PlaceLocation = PlaceLocation()
        PlaceLocation = place_location_form.save(commit=False)
        PlaceLocation.save()

        CivilStatus = CivilStatus()
        CivilStatus = civil_status_form.save(commit=False)
        CivilStatus.save()

        children_formset.save()

        CustomerAditionalData = CustomerAditionalData()
        CustomerAditionalData.customer = form.cleaned_data['customer']
        CustomerAditionalData.birth_place = BirthPlace
        CustomerAditionalData.place_location = PlaceLocation.user
        CustomerAditionalData.hobbies = form.cleaned_data['hobbies']
        CustomerAditionalData.sports = form.cleaned_data['sports']
        CustomerAditionalData.civil_status = CivilStatus
        CustomerAditionalData.interest_categories = form.cleaned_data['interest_categories']
        CustomerAditionalData.save()

        return redirect(self.get_success_url())

    def form_invalid(self, form, children_formset, birth_place_form, place_location_form,civil_status_form):
        return self.render_to_response(self.get_context_data(form=form, 
                                                             children_formset=children_formset, 
                                                             birth_place_form=birth_place_form,
                                                             place_location_form=place_location_form,
                                                             civil_status_form=civil_status_form))

class RegisterOrderView(View):
    form_class = OrderForm
    

    def get(self, request):
        form = self.form_class()
        return render(request, 'registerOrder.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
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
            form.save()
            return redirect('url_a_la_siguiente_vista')
        return render(request, self.template_name, {'form': form})
