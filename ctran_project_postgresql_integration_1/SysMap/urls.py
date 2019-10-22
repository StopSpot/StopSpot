from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='SysMap-home'),
    path('about/', views.about, name='SysMap-about'),
    path('single_stop/<str:lat>/<str:long>', views.single_stop, name='SysMap-single_stop'),
]
