from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404

# Create your views here.

class UmokkurView(TemplateView):
    template_name= 'umokkur/umokkur.html'
