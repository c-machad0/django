from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('-id')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__contains=search)
            
        return cars


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Lista de Carros'

        return context

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')    
class CarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_form.html'
    success_url = reverse_lazy('cars:car-list')


@method_decorator(login_required(login_url='login'), name='dispatch')    
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = reverse_lazy('cars:car-list')

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')    
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = reverse_lazy('cars:car-list')