from django.urls import path
from . import views

urlpatterns= [
    path('', views.IndexView.as_view(), name= 'index_sida'),
    path('fyrirspurn', views.FyrirspurnView.as_view(), name= 'fyrirspurn_sida'),
    path('fyrirspurn/takk', views.FyrirspurntakkView.as_view(), name= 'fyrirspurntakk_sida')
]
