from django.urls import path

from . import views

urlpatterns= [
    path('', views.index, name= 'index_sida'),
    path('gallery', views.gallery, name= 'gallery_sida'),
    path('gallery/<slug:slug>', views.verklys, name= 'verklys_sida'),
    path('fyrirspurn', views.FspurnView.as_view()),
    path('takk', views.TakkView.as_view(), name='takk_sida'),
    path('gallisti', views.GallistiView.as_view(), name='gallisti_sida'),
    path('gallisti/<int:pk>', views.DetbatView.as_view(), name='lysing_sida'),
    path('gallisti/myndir/<int:pk>', views.MyndirView.as_view(), name='myndir_sida')
]
