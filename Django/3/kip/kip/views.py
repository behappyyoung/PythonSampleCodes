from django.shortcuts import render
from mybackend import functions
import json


def index(request):
    title = 'index'
    return render(request, 'index.html',
                      {'title': title})