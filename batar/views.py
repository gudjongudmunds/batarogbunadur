from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from .forms import BatarfyrirspurnForm, BatarskraningForm
from .models import Batar, BatarFyrirspurn

# Create your views here.

from django.db.models import Q

class BatarlistiView(ListView):
    template_name = 'batar/batarlisti.html'
    model = Batar
    
    def get_queryset(self):
        queryset = Batar.objects.filter(birta=True)
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(Q(nafn__icontains=search_query))
        order_by = self.request.GET.get('order_by', '-rodun')  # Default to 'rodun'
        if order_by.startswith('-'):
            return queryset.order_by(order_by)
        else:
            order_direction = self.request.GET.get('direction', 'asc')
            if order_direction == 'desc':
                order_by = f'-{order_by}'
            return queryset.order_by(order_by)

    
class BaturlysingView(DetailView):
    template_name= 'batar/baturlysing.html'
    model= Batar
    slug_field = 'slug' 
    slug_url_kwarg = 'slug'
    
class BaturmyndirView(DetailView):
    template_name= 'batar/baturmyndir.html'
    model= Batar
    slug_field = 'slug' 
    slug_url_kwarg = 'slug'

class BaturfyrirspurnView(CreateView):
    model = BatarFyrirspurn
    form_class = BatarfyrirspurnForm
    template_name = 'batar/baturfyrirspurn.html'
    success_url= 'takk'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        boat = get_object_or_404(Batar, slug=self.kwargs.get('slug'))
        kwargs['boat'] = boat
        return kwargs

    def form_valid(self, form):
        boat = get_object_or_404(Batar, slug=self.kwargs.get('slug'))
        form.instance.nafn = boat
        return super().form_valid(form)
    
class BaturfyrirspurntakkView(TemplateView):
    template_name= 'batar/baturfyrirspurntakk.html'
    
class BataskraningView(CreateView):
    model = Batar
    form_class = BatarskraningForm
    template_name = 'batar/bataskraning.html'
    success_url= 'bataskraning/takk'

    def get_initial(self):
        initial = super().get_initial()
        initial['lys_vel_selj'] = (
            'Gerð vélar: \n'
            'Árgerð: \n'
            'Afl (hz/kw): \n'
            'Ganghraði: \n'
            'Keyrsla ca. (klst): \n'
            'Ástand: \n'
        )
        initial['lys_taeki_selj'] = (
            'Dýptarmælir: \n'
            'GPS: \n'
            'Plotter: \n'
            'Sjálfsstýring: \n'
            'Talstöð: \n'
            'Radar: \n'
            'Tölva: \n'
            'AIS: \n'
            'Annað:'
        )
        initial['lys_fylgi_selj'] = (
            'Veiðarfæri: \n'
            'Aflaheimildir (selja sér?): \n'
            'Kör (fjöldi?): \n'
            'Vagn (góður?): \n'
            'Annað sem fylgir?:'
        )
        initial['lys_annad_selj'] = (
            'Gerð báts (Sómi/Seigur/..?): \n'
            'Breyttur (lengdur?): \n'
            'Tekur í lest (tonn): \n'
            'Staðsetn. báts: \n'
            'Væntingar um verð: \n'
            'Annað/lýsing (gallar?):'
        )
        return initial
    
    def form_valid(self, form):
        for file_field in ['mynd1', 'mynd2', 'mynd3', 'mynd4', 'mynd5','mynd6', 'mynd7', 'mynd8','mynd9', 'mynd10', 'mynd11', 'mynd12', 'mynd13', 'mynd14','mynd15', 'mynd16', 'mynd17', 'mynd18', 'mynd19', 'mynd20']:
            print(self.request.FILES.get(file_field))
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['message_upph'] = "Með því að fá skráningar númer báts hér að neðan getur skipasali sótt opinberar upplýsingar um bátinn frá Samgöngustofu s.s. tegund, smíðaár, smíðastað, heimahöfn, brúttó tonn, lengd, breidd, vél, björgunarbát, haffæri, skoðanir, o.fl.  Það er því óþarfi að skrá þær upplýsingar hér að neðan."
        context['message_uppl'] = "ATH!  Eftir að upplýsingar hafa verið skráðar fer skipasali yfir skráninguna og verður í sambandi við eiganda áður en bátur er skráður."
        context['message_umb'] = "Skipasali þarf einnig umboð frá seljanda áritað með rafrænum skilríkjum áður en bátur er endanlega skráður sölulista."
        return context

    
class BataskraningtakkView(TemplateView):
    template_name= 'batar/bataskraningtakk.html'
    
