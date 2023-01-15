"""apps URL Configuration

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

import authentication.views
from purchases_auth import views

urlpatterns = [
#Administration
    path('admin/', admin.site.urls),
#Authentication
    path('', authentication.views.LoginPageView.as_view() , name='login'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('logout/', authentication.views.logout_user, name='logout'),
#Configuration
    path('config/', authentication.views.config_home, name='config-home'),
#Purchases_auth
    path('order/', views.order_list, name='order-list'),
    path('order/<int:id>/', views.order_detail, name='order-detail'),
    path('order/<int:id>/pending', views.order_detail, name='order-pending'),
    path('order/add/', views.order_create, name='order-create'),
]
