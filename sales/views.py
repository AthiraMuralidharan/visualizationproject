from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse

from sales.models import City


def home(request):
    return render(request, 'home.html')


def population_chart(request):
    labels = []
    data = []

    queryset = City.objects.values('country__name').annotate(country_population
                                                             =Sum('population')).order_by('-country_population')

    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])

    return JsonResponse(data={'labels': labels, 'data': data, })


def testing(request):
    return render(request, 'test.html')


def datatable_static(request):
    country_name = []
    country_population = []

    queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by(
        '-country_population')

    for entry in queryset:
        country_name.append(entry['country__name'])
        country_population.append(entry['country_population'])

    data = zip(country_name, country_population)
    return render(request, 'datatable/datatable_static.html', {'data': data})
