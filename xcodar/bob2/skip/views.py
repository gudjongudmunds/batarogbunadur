from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView

# Create your views here.

class CrateSkipView(CreateView):
    template_name= ''