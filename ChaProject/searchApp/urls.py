from django.urls import path
from . import views
urlpatterns=[
    path('services1/', views.services1, name='services1'),
    path('services1/<city>/', views.services1_city, name='services1_city'),
    path('services1/<city>/<town>/', views.services1_town, name='services1_town'),
    path('services1/<city>/<town>/<name>', views.services1_name, name='services1_name'),
    path('services1/<city>/<town>/<name>/search/', views.services1_search, name='services1_search'),
    path('services2/', views.services2, name='services2'),
    path('services3/', views.services3, name='services3'),
    path('tt/', views.tt, name='tt'), # 지도 테스트. 나중에 지우기
]