from django.urls import include, path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('list/',views.list,name='list'),
    path('match/<int:pk>',views.match,name='match'),
    path('match/<int:match>/<int:event>',views.event,name='event'),
]
