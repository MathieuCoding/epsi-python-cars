from django.shortcuts import render
from .models import Car
from .forms import CarForm

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'list_cars/cars_list.html', {'cars': cars})

def car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    return render(request, 'list_cars/car_detail.html', {'car': car})

def car_rating(request, pk):
    form = CarForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # car = Car.objects.get(pk=pk)
            # car.rating = form.cleaned_data['rating']
            # car.save()
            form.save()
        else:
            form = CarForm()
    return render(request, 'list_cars/car_detail.html', {'form': form})