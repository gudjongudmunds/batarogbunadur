from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .models import Gallery, Fyrirspurn

# Create your views here.
 
def index(request):
    sidasta_verk= Gallery.objects.all().order_by('-date')[:3]
    return render(request, 'gallery/index.html', {
        'verkin': sidasta_verk
       })

def gallery(request):
    gallery_listi= Gallery.objects.all().order_by('-date')
    return render(request, 'gallery/gallery.html',{
       'galler': gallery_listi
       })

def verklys(request, slug):
    id_ve= get_object_or_404(Gallery, slug=slug)
    return render(request, 'gallery/verklys.html',{
       'veve':id_ve
       })

class FspurnView(CreateView):
    model= Fyrirspurn
    fields= '__all__'
    template_name= 'gallery/fspurn.html'
    success_url= '/takk'
    

class TakkView(TemplateView):
    template_name= 'gallery/takk.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["skilabod"]= 'Þetta svínvirkar!' 
        return context
    
class GallistiView(ListView):
    template_name= 'gallery/gallisti.html'
    model= Gallery
        
class DetbatView(DetailView):
    template_name= 'gallery/detbat.html'
    model= Gallery
    
class MyndirView(DetailView):
    template_name= 'gallery/pic.html'
    model= Gallery
