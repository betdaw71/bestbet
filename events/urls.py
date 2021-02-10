from django.urls import include, path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('match/',views.list,name='list'),
    path('match/<str:match_id>',views.match,name='match'),
    path('match/<str:match_id>/<int:event>',views.event,name='event'),
]
