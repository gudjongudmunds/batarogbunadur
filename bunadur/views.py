from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from .forms import BunadurfyrirspurnForm, BunadurskraningForm
from .models import Bunadur, BunadurFyrirspurn

# Create your views here.

class BunadurlistiView(ListView):
    template_name= 'bunadur/bunadurlisti.html'
    model= Bunadur
    
    def get_queryset(self):
        queryset = Bunadur.objects.filter(birta=True)
        order_by = self.request.GET.get('order_by', '-rodun')  # Default to 'nafn'
        order_direction = self.request.GET.get('direction', 'asc')
        
        if order_direction == 'desc':
            order_by = f'-{order_by}'
        
        return queryset.order_by(order_by)
        
class BunadurlysingView(DetailView):
    template_name= 'bunadur/bunadurlysing.html'
    model= Bunadur
    slug_field = 'slug' 
    slug_url_kwarg = 'slug'
    
class BunadurmyndirView(DetailView):
    template_name= 'bunadur/bunadurmyndir.html'
    model= Bunadur
    slug_field = 'slug' 
    slug_url_kwarg = 'slug'

class BunadurfyrirspurnView(CreateView):
    model = BunadurFyrirspurn
    form_class = BunadurfyrirspurnForm
    template_name = 'bunadur/bunadurfyrirspurn.html'
    success_url= 'takk'


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        boat = get_object_or_404(Bunadur, slug=self.kwargs.get('slug'))
        kwargs['boat'] = boat
        return kwargs

    def form_valid(self, form):
        boat = get_object_or_404(Bunadur, slug=self.kwargs.get('slug'))
        form.instance.nafn = boat
        print(form.fields['boat_name'].label)  # Debugging: Print the label to check
        return super().form_valid(form)

    
class BunadurfyrirspurntakkView(TemplateView):
    template_name= 'bunadur/bunadurfyrirspurntakk.html'
    
class BunadurskraningView(CreateView):
    model = Bunadur
    form_class = BunadurskraningForm
    template_name = 'bunadur/bunadurskraning.html'
    success_url= 'bunadarskraning/takk'
    
    def get_initial(self):
        initial = super().get_initial()
        initial['lys_selj'] = (
            'Staðsetning: \n'
            'Nýtt/notað/árg.?: \n'
            'Skipti?: \n'
            'Verðhugmyndir: \n'
            'Annað/lýsing: \n'
        )
        return initial
    
    def form_valid(self, form):
        for file_field in ['mynd1', 'mynd2', 'mynd3', 'mynd4', 'mynd5','mynd6']:
            print(self.request.FILES.get(file_field))
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['message_upplys'] = "Gott að fá nokkuð ítarlegar upplýsingar um búnað."
        context['message_upplysned'] = "ATH!  Eftir að upplýsingar hafa verið skráðar fer skipasali yfir skráninguna og verður í sambandi við eiganda áður en búnaður er skráður á söluskrá."
        return context
    
class BunadurskraningtakkView(TemplateView):
    template_name= 'bunadur/bunadurskraningtakk.html'