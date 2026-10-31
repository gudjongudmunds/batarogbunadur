from django.urls import path
from . import views

urlpatterns= [
    path('', views.GjaldskraView.as_view(), name= 'gjaldskra_sida')
]
