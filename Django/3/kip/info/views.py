from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ContentForm
from django.contrib import messages
from django.core import serializers
# Create your views here.

# Contents
# @login_required()
def add_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        try:
            if form.is_valid():
                form.save()
            else:
                messages.error(request, form.errors)
                return HttpResponseRedirect('/')
        except:
            messages.error(request, form.errors)
            return HttpResponseRedirect('/')
    else:
        form = ContentForm(request.POST)

    # functions.f_access_log(request, 'access')
    return render(request, 'Info/Contents.html', {'form': form })


def contents_list(request):
    contents = Content.objects.all()

    return render(request, 'Info/ContentsList.html', {'contents': contents})


### Category
def category_list(request):
    category_list = Category.objects.all()
    jsonstring_category = serializers.serialize('json', category_list)
    return render(request, 'Info/ContentsList.html', {'category_list': jsonstring_category})

def add_category(request):
    if request.method == 'POST':
        try:
            pass
        except:
            return ''

    else:
        messages.error(request, 'only POST')

    return render(request, 'Info/Contents.html', {})

