from django.urls import path
from . import views

urlpatterns= [
    path('', views.AflaheimlistiView.as_view(), name= 'aflaheimlisti_sida'),
    path('<slug:slug>/', views.AflaheimlysingView.as_view(), name= 'aflaheimlysing_sida'),
    path('<slug:slug>/myndir', views.AflaheimmyndirView.as_view(), name= 'aflaheimmyndir_sida'),
    path('<slug:slug>/fyrirspurn/', views.AflaheimfyrirspurnView.as_view(), name= 'aflaheimfyrirspurn_sida'),
    path('<slug:slug>/fyrirspurn/takk', views.AflaheimfyrirspurntakkView.as_view(), name= 'aflaheimfyrirspurntakk_sida'),
    path('aflaheimildirskraning', views.AflaheimskraningView.as_view(), name= 'aflaheimskraning_sida'),
    path('aflaheimildirskraning/takk', views.AflaheimskraningtakkView.as_view(), name= 'aflaheimskraningtakk_sida')
]
