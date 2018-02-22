from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from homepage import models as cmod
from .. import dmp_render, dmp_render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from .. import dmp_render, dmp_render_to_string
from django import forms

@view_function
def process_request(request):
    context = {

    }
    return dmp_render(request, 'textTest.html', context)