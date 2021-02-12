"""bet URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect
from rest_framework import routers
from events import views

router = routers.DefaultRouter()
router.register(r'match/(?P<sport>.*)', views.MatchViewSet)
router.register(r'event/(?P<match_id>.*)', views.EventViewSet, basename='MyModel')

# def main(request):
#     if request.user.is_authentificated:
#         return redirect('list')
#     else:
#         return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',main,name='main'),
    path('account/',include('account.urls')),
    path('events/',include('events.urls')),
    path('api/', include(router.urls)),
    path('api-auth/',include('rest_framework.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
