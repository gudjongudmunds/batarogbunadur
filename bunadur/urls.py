from django.urls import path
from . import views

urlpatterns= [
    path('', views.BunadurlistiView.as_view(), name= 'bunadurlisti_sida'),
    path('<slug:slug>/', views.BunadurlysingView.as_view(), name= 'bunadurlysing_sida'),
    path('<slug:slug>/myndir', views.BunadurmyndirView.as_view(), name= 'bunadurmyndir_sida'),
    path('<slug:slug>/fyrirspurn/', views.BunadurfyrirspurnView.as_view(), name= 'bunadurfyrirspurn_sida'),
    path('<slug:slug>/fyrirspurn/takk', views.BunadurfyrirspurntakkView.as_view(), name= 'bunadurfyrirspurntakk_sida'),
    path('bunadarskraning', views.BunadurskraningView.as_view(), name= 'bunadurskraning_sida'),
    path('bunadarskraning/takk', views.BunadurskraningtakkView.as_view(), name= 'bunadurskraningtakk_sida')
]