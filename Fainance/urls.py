from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('costEdit/', views.costEditview),
    path('costList', views.costListView),
    
  
]
