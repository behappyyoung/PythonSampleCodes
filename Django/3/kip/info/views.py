from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from django.core import serializers
from kip import settings
import json
# Create your views here.
global_context = {
        'LOCAL': settings.LOCAL,
        # 'GIT_BRANCH': settings.GIT_BRANCH,
        # 'GIMS_VERSION': settings.KIP_VERSION,
}


# Contents
# @login_required()
def add_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.error(request, 'Saved')
                return HttpResponseRedirect('/Info/')
            else:
                messages.error(request, form.errors)
                form = ContentForm(request.POST)
        except:
            messages.error(request, form.errors)
            form = ContentForm(request.POST)
    else:
        form = ContentForm()

    # functions.f_access_log(request, 'access')
    return render(request, 'Info/Contents.html', {'form': form })


def contents_list(request):
    title = 'Info - Contents'

    contents = Content.objects.all()

    return render(request, 'Info/ContentsList.html', {'contents': contents, title: title})


### Category
def categories(request):
    jsonstring_category = []
    try:
        category = Category.objects.filter().values()
        for c in category:
            parent_id = c.get('parent_id') or '--'
            jsonstring_category.append({'id': c.get('id'), 'name': c.get('name')})

    except Exception as e:
        jsonstring_category = []

    context = global_context
    title = 'Categories'
    templates = 'Info/Category/Category.html'
    context.update({'title': title, 'category_list': jsonstring_category})
    return render(request, templates, context)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.error(request, 'Saved')
                return HttpResponseRedirect('/Info/Categories/')
            else:
                messages.error(request, form.errors)
                form = CategoryForm(request.POST)
        except:
            messages.error(request, form.errors)
            form = CategoryForm(request.POST)

    else:
        form = CategoryForm()

    return render(request, 'Info/Category/AddCategory.html', {'form': form})

