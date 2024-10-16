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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

from apps.main.views import home, contact, checkout, cart

from apps.categories.views import category
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # ========== set language =========
    path('searchs/', include('apps.general.urls', namespace='searchs')),

    path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns += i18n_patterns(
    # ========== about urls ===========
    path('about/', include('apps.abouts.urls', namespace='about')),
    path('wishlists/', include('apps.wishlists.urls', namespace='wishlist')),
    path('comments/', include('apps.comments.urls', namespace='comments')),

    path('admin/', admin.site.urls),
    path('', home, name='home-page'),

    path('contact/', contact, name='contact-page'),
    path('checkout/', checkout, name='checkout-page'),
    path('cart/', cart, name='cart-page'),
    path('products/', include('apps.products.urls', namespace='products')),
    path('category/', category, name='category-page'),

    path('authentications/', include('apps.authentication.urls', namespace='authentications')),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

)
# if settings.DEBUG:
