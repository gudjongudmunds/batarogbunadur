from django.urls import path
from . import views

urlpatterns= [
    path('', views.UmokkurView.as_view(), name= 'umokkur_sida')
]
