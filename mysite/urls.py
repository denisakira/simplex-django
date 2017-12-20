from mysite import views
from django.urls import path, include


urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index),
    path('simplex/', views.get_simplex),
    path('thanks/', views.thanks),
    path('gomory/',views.gomory, name='gomory'),
]