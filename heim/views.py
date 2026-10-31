from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.edit import CreateView
from batar.models import Batar
from bunadur.models import Bunadur
from aflaheimildir.models import Aflaheim
from .models import Fyrirspurn
from .forms import FyrirspurnForm


class FyrirspurnView(CreateView):
    model = Fyrirspurn
    form_class = FyrirspurnForm
    template_name = 'heim/fyrirspurn.html'
    success_url= 'fyrirspurn/takk'
    
class FyrirspurntakkView(TemplateView):
    template_name= 'heim/fyrirspurntakk.html'
    

class IndexView(TemplateView):
    template_name = 'heim/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filter and retrieve data from each model where birta=True
        context['batar_list'] = Batar.objects.filter(birta=True).order_by('-nyskr_dags')[:2]
        context['bunadur_list'] = Bunadur.objects.filter(birta=True).order_by('-nyskr_dags')[:2]
        context['aflaheim_list'] = Aflaheim.objects.filter(birta=True).order_by('-nyskr_dags')[:2]
        return context

