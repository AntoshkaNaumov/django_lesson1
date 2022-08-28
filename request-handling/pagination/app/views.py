from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


with open('data-398-2018-08-30.csv', 'r') as file:
    reader = csv.DictReader(file)
    content = []
    for item in reader:
        content.append(item)

def bus_stations(request):
    paginator = Paginator(content, 15)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': content,
        'page': page,
    }
    return render(request, 'index.html', context)