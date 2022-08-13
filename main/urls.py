from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('explore/', views.explore, name='explore'),
    path('SignUp/', views.SignUp, name='SignUp'),
    path('reg/', views.reg, name='reg')
]
