# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def privacy(request):
    """
        Privacy Page
    """
    # logging(request, 'access')
    return render(request, 'privacy.html', {'title':'Privacy'})