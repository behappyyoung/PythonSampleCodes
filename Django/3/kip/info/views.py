from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ContentForm
from django.contrib import messages
from django.core import serializers
from kip import settings
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
    title = 'Info - Contents'

    contents = Content.objects.all()

    return render(request, 'Info/ContentsList.html', {'contents': contents, title: title})


### Category
def categories(request):
    category_list = Category.objects.all()
    jsonstring_category = serializers.serialize('json', category_list)
    context = global_context
    title = 'Categories'
    templates = 'Info/Category/Category.html'
    context.update({'title': title, 'category_list': jsonstring_category})
    return render(request, templates, context)

def add_category(request):
    if request.method == 'POST':
        try:
            pass
        except:
            return ''

    else:
        messages.error(request, 'only POST')

    return render(request, 'Info/Contents.html', {})

