from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from .forms import AflaheimfyrirspurnForm, AflaheimskraningForm
from .models import Aflaheim, AflaheimFyrirspurn

# Create your views here.

class AflaheimlistiView(ListView):
    template_name= 'aflaheimildir/aflaheimlisti.html'
    model= Aflaheim
    
    def get_queryset(self):
        queryset = Aflaheim.objects.filter(birta=True)
        order_by = self.request.GET.get('order_by', '-rodun')  
        order_direction = self.request.GET.get('direction', 'asc')
        
        if order_direction == 'desc':
            order_by = f'-{order_by}'
        
        return queryset.order_by(order_by)
    
class AflaheimlysingView(DetailView):
    template_name= 'aflaheimildir/aflaheimlysing.html'
    model= Aflaheim
    slug_field = 'slug' 
    slug_url_kwarg = 'slug'
    
class AflaheimmyndirView(DetailView):
    template_name= 'aflaheimildir/aflaheimmyndir.html'
    model= Aflaheim
    slug_field = 'slug' 
    slug_url_kwarg = 'slug'

class AflaheimfyrirspurnView(CreateView):
    model = AflaheimFyrirspurn
    form_class = AflaheimfyrirspurnForm
    template_name = 'aflaheimildir/aflaheimfyrirspurn.html'
    success_url= 'takk'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        boat = get_object_or_404(Aflaheim, slug=self.kwargs.get('slug'))
        kwargs['boat'] = boat
        return kwargs

    def form_valid(self, form):
        boat = get_object_or_404(Aflaheim, slug=self.kwargs.get('slug'))
        form.instance.nafn = boat
        return super().form_valid(form)
    
class AflaheimfyrirspurntakkView(TemplateView):
    template_name= 'aflaheimildir/aflaheimfyrirspurntakk.html'
    
class AflaheimskraningView(CreateView):
    model = Aflaheim
    form_class = AflaheimskraningForm
    template_name = 'aflaheimildir/aflaheimskraning.html'
    success_url= 'aflaheimildirskraning/takk'
    
    def get_initial(self):
        initial = super().get_initial()
        initial['lys_selj'] = (
            'Verð samtals: \n'
            'Birta verð eða biðja um tilboð?: \n'
            'Annað/lýsing: \n'
        )
        return initial
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['message_aflah'] = "ATH!  Eftir að upplýsingar hafa verið skráðar fer skipasali yfir skráninguna og verður í sambandi við eiganda áður en aflaheimildir eru skráðar á söluskrá."
        return context
    
class AflaheimskraningtakkView(TemplateView):
    template_name= 'aflaheimildir/aflaheimskraningtakk.html'