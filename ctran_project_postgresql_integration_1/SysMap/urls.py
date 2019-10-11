from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='SysMap-home'),
    path('about/', views.about, name='SysMap-about'),
]
