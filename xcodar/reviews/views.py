from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Review, Boats

# Create your views here.

# views.py
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from .models import Review, Boats
from .forms import ReviewForm

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url= '/thank-you'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        boat = get_object_or_404(Boats, pk=self.kwargs.get('pk'))
        kwargs['boat'] = boat
        return kwargs

    def form_valid(self, form):
        boat = get_object_or_404(Boats, pk=self.kwargs.get('pk'))
        form.instance.rev_batur = boat
        return super().form_valid(form)


class BoatsListView(ListView):
    template_name= 'reviews/boatslist.html'
    model= Boats
    
class BoatDetailView(DetailView):
    template_name= 'reviews/boatdetail.html'
    model= Boats
    

def thank_you(request):
    return render(request, 'reviews/thank_you.html')
    


