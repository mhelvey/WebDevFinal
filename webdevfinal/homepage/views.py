import datetime
from django.shortcuts import render, render_to_response
from django.template import Context, loader
from django.http import HttpResponse
from homepage import models as hmod
from django import forms
import os.path


# Create your views here.
l = loader

def base(request):
    t = l.get_template('base.html')
    c = Context({

    })

    return HttpResponse(t.render(c))

def education(request):
    t = l.get_template('education.html')
    c = Context({

    })

    return HttpResponse(t.render(c))

def experience(request):
    t = l.get_template('experience.html')
    c = Context({

    })

    return HttpResponse(t.render(c))

def adventures(request):
    images = hmod.Panorama.objects.all()
    t = l.get_template('adventures.html')
    c = Context({
        'images': images
    })

    return HttpResponse(t.render(c))

def contact(request):
    t = l.get_template('contact.html')
    c = Context({

    })

    return HttpResponse(t.render(c))