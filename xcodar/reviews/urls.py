from django.urls import path
from . import views
from .views import BoatDetailView, ReviewView

urlpatterns = [
    path('boats/<int:pk>/review/', ReviewView.as_view(), name='boat_review'),
    path('thank-you', views.thank_you),
    path('boatslist', views.BoatsListView.as_view()),
    path('boats/<int:pk>/', BoatDetailView.as_view(), name='boat_detail')
]
