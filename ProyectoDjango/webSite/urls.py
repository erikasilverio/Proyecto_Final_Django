"""
URL configuration for webSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

#from django.contrib import admin
#from django.urls import path,include
#from . import views
#from django.views.generic import RedirectView
#from myproyect import views
#from django.contrib.auth import views as auth_views





from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from django.contrib.auth import views as auth_views
from myproyect import views




from myproyect.views import (   
    login,
    registro_user,
    index,
    perfil,
    garage,
    venta_auto,
    contacto
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='index/', permanent=False)),  
    path('index/', views.index, name='index'),
    #registro user
    path('registro_user/', registro_user, name='registro_usuario'),

    path('mapa/', views.mapa_view, name='mapa'),
    # path('login/', login, name='login'),
    #path('index/', index, name='index'),
    path('perfil.html', perfil, name='perfil'),
    path('registro_user/', registro_user, name='registro_user'),
    path('garage/', garage, name='garage'),
    path('venta_auto/', venta_auto, name='venta_auto'),
    path('contacto/', contacto, name='contacto'),   
    # login y logout
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('logout/', views.custom_logout, name='logout'),



    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
]


###
# urlpatterns = [
  #  path('admin/', admin.site.urls),
  #  path('',views.casa,name='casa'),

    # login, perfil , registro_user
  #  path('', RedirectView.as_view(url='index/', permanent=False)),     
  #  path('', login, name='login'),    
  #  path('perfil.html', perfil, name='perfil'),
  #  path('registro_user/', registro_user, name='registro_user'), 
    
  #  path('login/', auth_views.LoginView.as_view(), name='login'),
  #  path('logout/', views.custom_logout, name='logout'),

  
# ] 
###
#------------------------------------------

