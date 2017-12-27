from mysite import views
from django.urls import path, include


urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index),
    path('simplex/', views.get_simplex),
    path('simplex3/', views.simplex3, name='simplex3'),
    path('get_simplex3/',views.get_simplex3),
    path('simplexduasfases/',views.simplexduasfases),
    path('simplex3duasfases/',views.simplex3duasfases),
    path('get_simplexduasfases/',views.get_simplexduasfases,name='get_simplexduasfases'),
    path('get_simplex3duasfases/',views.get_simplex3duasfases),
    path('gomory/', views.gomory, name='gomory'),
    path('get_gomory/',views.get_gomory),
    path('gomory3/', views.gomory3),
]