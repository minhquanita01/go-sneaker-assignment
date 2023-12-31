"""
URL configuration for go_sneaker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from go_shoes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('go_shoes/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('go_shoes/inc_quantity/', views.inc_quantity_cart, name='inc_quantity'),
    path('go_shoes/dec_quantity/', views.desc_quantity_cart, name='dec_quantity'),
    path('go_shoes/remove_cart_item/', views.remove_cart_item, name='remove_cart_item'),
]
