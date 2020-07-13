from django.shortcuts import render
from sample import settings

##from django.http import HttpResponse

simple_context = {
        'GIT_BRANCH': settings.GIT_BRANCH,
}

def index(request):
    title = 'Simple Django Sample Page'
    context = simple_context
    context.update({'title': title })
    return render(request, 'index.html', context)
