"""
URL configuration for mahir project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from gas_service import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('admin/', admin.site.urls),
    path('requests/', views.service_request_list, name='service_request_list'),
    path('requests/new/', views.create_service_request, name='create_service_request'),
]
