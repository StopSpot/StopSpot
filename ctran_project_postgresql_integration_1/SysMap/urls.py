from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='SysMap-home'),
    path('about/', views.about, name='SysMap-about'),
    path('single_stop/<str:lat>/<str:long>/<str:code>/', views.single_stop, name='SysMap-single_stop'),
    path('top/<str:code>/', views.stop, name='top'),
    path('routes', views.routes, name='routes'),
    path('single_route/<str:route>/', views.single_route, name='single_route'),
]
