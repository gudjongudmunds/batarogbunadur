from django.urls import path
from . import views

urlpatterns= [
    path('', views.BatarlistiView.as_view(), name= 'baturlisti_sida'),
    path('<slug:slug>/', views.BaturlysingView.as_view(), name= 'baturlysing_sida'),
    path('<slug:slug>/myndir', views.BaturmyndirView.as_view(), name= 'baturmyndir_sida'),
    path('<slug:slug>/fyrirspurn/', views.BaturfyrirspurnView.as_view(), name= 'baturfyrirspurn_sida'),
    path('<slug:slug>/fyrirspurn/takk', views.BaturfyrirspurntakkView.as_view(), name= 'baturfyrirspurntakk_sida'),
    path('bataskraning', views.BataskraningView.as_view(), name= 'bataskraning_sida'),
    path('bataskraning/takk', views.BataskraningtakkView.as_view(), name= 'bataskraningtakk_sida')
]
