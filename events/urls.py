from django.urls import include, path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('match/<str:sport>',views.list,name='list'),
    path('match/<str:sport>/<str:match_id>',views.match,name='match'),
    path('match/<str:sport>/<str:match_id>/<int:event>',views.event,name='event'),
    path('match/<str:sport>/<str:match_id>/<int:event>/express',views.express,name='express'),
    path('match/<str:sport>/<str:match_id>/<int:event>/express/create',views.express_add,name='express_add'),
]
