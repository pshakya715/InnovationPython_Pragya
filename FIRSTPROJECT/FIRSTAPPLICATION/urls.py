from django.urls import path

from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('TEMPLATE_PATH/', views.firstapp, name='firstapp'),
]