from django.urls import path
from . import views

urlpatterns = [
    path('', views.tinys_home, name='tinys_home'),
    path('create', views.create, name='create'),
]