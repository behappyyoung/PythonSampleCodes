# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import RequestContext
from django.http import (HttpResponse, HttpResponseRedirect,
                         HttpResponseServerError)

from django.contrib import messages
import urllib2
import ssl, json
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Create your views here.
from loomui import settings
from .models import Workflows


def custom_proc(request):
    return {
        'LOOMURL': settings.LOOMURL,
        'LOOMURLS': settings.LOOMURLS
    }

def workflows(request):
    try:
        loom_workflows_json = urllib2.urlopen(settings.LOOMURLS['workflows'], context=ctx).read()
        loom_workflows = json.loads(loom_workflows_json)
    except Exception as e:
        loom_workflows =[]
        message = "could not fetch %s" % settings.LOOMURLS['workflows']
        messages.error(request, message)

    # save workflow in DB
    workflows =[]
    c_workflows = Workflows.objects.all()
    active_wf = []
    for lw in loom_workflows:
        w_exist = False
        uuid = lw.get('uuid')
        name = lw.get('name')
        label = lw.get('label')
        is_leaf = lw.get('is_leaf')
        json_inputs = json.dumps(lw.get('inputs'))
        json_fixed_inputs = json.dumps(lw.get('fixed_inputs'))
        ordertype = None
        version = None
        desc = None
        active_wf.append(uuid)
        type = 'leaf' if is_leaf else 'workflow'
        for cw in c_workflows:
            if uuid == cw.workflow_id:
                w_exist = True
                cw.name = name
                cw.inputs = json_inputs
                cw.fixed_inputs = json_fixed_inputs
                cw.type = type
                cw.status = 'A'
                version = cw.version
                cw.save()
                break

        if not w_exist and not is_leaf:
            new_workflow = Workflows(workflow_id=uuid, name=name, inputs=json_inputs, fixed_inputs=json_fixed_inputs, type=type, status='A')
            new_workflow.save()

        workflows.append({'uuid': uuid, 'name': name, 'version': version, 'ordertype': ordertype, 'desc': desc,
                          'inputs': json_inputs, 'fixed_inputs': json_fixed_inputs, 'type': type})

    # make inactive those are not in loom
    for cw in c_workflows:
        if cw.workflow_id not in active_wf:
            cw.status = 'I'
            cw.save()

    # logging(request, 'access')
    return render(request, 'workflows.html', {'workflows':json.dumps(workflows), 'processors':[custom_proc]})
