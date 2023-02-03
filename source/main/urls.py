"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from api_v1.views import sub, add, mul, div, get_token_view
from webapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sub/', sub, name='sub'),
    path('add/', add, name='add'),
    path('mul/', mul, name='mul'),
    path('div/', div, name='div'),
    path('get_token/', get_token_view),
    path('', index, name='index')
]
