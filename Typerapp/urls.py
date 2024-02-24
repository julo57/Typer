
from django.urls import path
from . import views


urlpatterns = [
   path('', views.main, name='main'),
   
   path('base/', views.base, name='base'),
  
path('read_file2/', views.read_file2, name='read_file2'),
   path('test/', views.test, name='test'),
   
]
