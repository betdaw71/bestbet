""" bet URL Configuration

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

from django.urls import include, path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('',views.home,name='home'),
    path('change_username/<str:username>',views.change_username,name='change_username'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('identify/',views.identify,name='identify'),
    path('history/',views.history,name='history'),
    path('password/',views.change_password,name='change_password'),
    path('signup_activate/<int:id>/',views.signup_activate,name='signup_activate'),
    path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    path('activate/<str:uidb64>/<str:token>/',views.activate, name='activate'),
    path('password_reset/', auth_views.PasswordResetView.as_view(html_email_template_name='account/password_reset_html_email.html'),name='reset_password'),
    path('password_reset_confirm/<str:uidb64>/<str:token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),
    path('number_change/<int:id>',views.number_change,name='number_change')
]
