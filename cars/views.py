from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search: # Verifica se é não nula
        cars = cars.filter(model__contains=search)

    return render(request, 
                  'cars.html',
                  {'cars': cars})