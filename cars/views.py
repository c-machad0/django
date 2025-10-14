from django.shortcuts import render

def cars_view(request):
    return render(request, 'cars.html')