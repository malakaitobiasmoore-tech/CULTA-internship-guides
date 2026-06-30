from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guide/<slug:name>/', views.guide, name='guide'),
]