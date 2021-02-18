from django.urls import path
from . import views
urlpatterns=[
    path('review_academy/', views.review_academy, name='review_academy'),
    path('review_testsite/', views.review_testsite, name='review_testsite'),

    path('read_academy/', views.read_academy, name='read_academy'),
    path('read_testsite/', views.read_testsite, name='read_testsite'),

    path('update_academy/', views.update_academy, name='update_academy1'),
    path('update_academy/<int:id>/', views.update_academy, name='update_academy2'),
    path('update_testsite/', views.update_testsite, name='update_testsite1'),
    path('update_testsite/<int:id>/', views.update_testsite, name='update_testsite2'),

    path('delete_academy/', views.delete_academy, name='delete_academy'),
    path('delete_testsite/', views.delete_testsite, name='delete_testsite'),

    path('create_academy/', views.create_academy, name='create_academy'),
    path('create_testsite/', views.create_testsite, name='create_testsite'),

    path('get_academy_town/', views.get_academy_town, name='get_academy_town'),
    path('get_academy_name/', views.get_academy_name, name='get_academy_name'),
    path('get_testsite_name/', views.get_testsite_name, name='get_testsite_name'),

    path('get_academy_password/', views.get_academy_password, name='get_academy_password'),
    path('get_testsite_password/', views.get_testsite_password, name='get_testsite_password'),
]