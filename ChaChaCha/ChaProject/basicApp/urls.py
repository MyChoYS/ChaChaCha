from django.urls import path
from . import views
urlpatterns=[
    path('home/', views.home, name='home'),
    path('information/', views.information, name='information'),
    path('information_0/', views.information_0, name='information_0'),
    path('information_1/', views.information_1, name='information_1'),
    path('information_2/', views.information_2, name='information_2'),
    path('information_2_1/', views.information_2_1, name='information_2_1'),
    path('information_2_2/', views.information_2_2, name='information_2_2'),
    path('information_2_3/', views.information_2_3, name='information_2_3'),
    path('information_2_4/', views.information_2_4, name='information_2_4'),
    path('information_3/', views.information_3, name='information_3'),
    path('information_3_1/', views.information_3_1, name='information_3_1'),
    path('information_3_2/', views.information_3_2, name='information_3_2'),
    path('information_4/', views.information_4, name='information_4'),
    path('information_4_1/', views.information_4_1, name='information_4_1'),
    path('information_4_2/', views.information_4_2, name='information_4_2'),
    path('information_4_3/', views.information_4_3, name='information_4_3'),
    path('information_5/', views.information_5, name='information_5'),
    path('information_6/', views.information_6, name='information_6'),

]