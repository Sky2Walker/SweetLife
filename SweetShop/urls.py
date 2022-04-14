"""SweetShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^cart/', include(('cart.urls', 'cart'),namespace='cart')),
    path(r'^basket_adding', include(('orders.urls', 'orders'), namespace='orders')),
    path(r'', include(('shop.urls', 'shop'), namespace='shop')),
    path(r'store', include(('shop.urls', 'shop'), namespace='shop')),
    path(r'news', include(('shop.urls', 'shop'), namespace='shop')),
    path(r'about', include(('shop.urls', 'shop'), namespace='shop')),
    path(r'contact', include(('shop.urls', 'shop'), namespace='shop')),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
