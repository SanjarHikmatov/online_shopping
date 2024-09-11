"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.main.views import home, shop, contact, detail, checkout, cart, about, login_page

from apps.categories.views import category
from apps.registers.views import register
from config import settings
from config.settings import STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home-page'),
    path('detail/', detail, name='detail-page'),
    path('contact/', contact, name='contact-page'),
    path('checkout/', checkout, name='checkout-page'),
    path('cart/', cart, name='cart-page'),
    path('shop/', shop, name='shop-page'),
    path('category/', category, name='category-page'),
    path('register/', register, name='register-page'),
    path('about/', about, name='about-page'),
    path('login-page/', login_page, name='login-page'),

]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)