from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('POST_DELETE/', views.deleteapp, name='deleteapp'),
    path('POST_FORM/', views.formapp, name='formapp'),
    path('POST_LIST/', views.listapp, name='listapp'),
]