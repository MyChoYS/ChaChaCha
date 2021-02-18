from django.urls import path
from . import views
urlpatterns=[
    path('', views.test, name='test'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('components/', views.components, name='components'),
]