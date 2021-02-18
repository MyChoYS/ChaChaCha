"""ChaProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import basicApp
urlpatterns = [
    # homeApp은 지우고.
    # path 이름 좀 바꿔주기.
    path('/',basicApp.views.home),
    path('admin/', admin.site.urls),
    #path('homeApp/', include('homeApp.urls')), # homeApp은 그냥 테스트용 앱...!
    path('basicApp/', include('basicApp.urls')),
    path('searchApp/', include('searchApp.urls')),
    path('bbsApp/', include('bbsApp.urls')),

]
