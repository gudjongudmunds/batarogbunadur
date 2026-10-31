from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .models import Gjaldskra

# Create your views here.

class GjaldskraView(ListView):
    template_name= 'gjaldskra/gjaldskra.html'
    model= Gjaldskra
    
    def get_queryset(self):
        return Gjaldskra.objects.filter(birta=True)