"""oxygen_cylinder_leads URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url,include
from oxygen_cylinder_tracker.views import Oxygen_cylinder_view,User_view_set
from rest_framework.routers import  DefaultRouter
router=DefaultRouter()
router.register('cylinder_view_set',User_view_set)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    url(r'^oxygen/',include('rest_framework.urls')),
]
