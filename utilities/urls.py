from django.urls import path
from . import views

urlpatterns = [
    path('original/', views.original, name='original'),
    path('translated/', views.translated, name='translated'),
    path('ascii_make/', views.ascii_make, name='ascii_make'),
    path('ascii_new/', views.ascii_new, name='ascii_new'),
    path('today/', views.today, name='today'),
    path('graduation/', views.graduation, name='graduation'),
    path('bye/', views.bye, name='bye'),
    path('imagepick/', views.imagepick, name='imagepick'),
    path('', views.index, name='index'),
    ]