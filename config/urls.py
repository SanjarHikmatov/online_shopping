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

from apps.main.views import home, shop, contact, detail, checkout, cart

from apps.categories.views import category
from django.conf import settings
from django.conf.urls.static import static
from apps.authentication import views as auth_views

from apps.general.views import set_language, search
from apps.wishlists import views
urlpatterns = [

    path('__debug__/', include('debug_toolbar.urls')),
]


urlpatterns += i18n_patterns(
# ========== about urls ===========
    path('about/', include('apps.abouts.urls', namespace='about')),
    # path('wishlists/', include('apps.wishlists.urls', namespace='wishlist')),
    path('wishlist_add_page/', views.view_wishlist, name='wishlist-add-page'),
    path('wishlist-page', views.wishlist_page, name='wishlist-page'),
    path('admin/', admin.site.urls),
    path('', home, name='home-page'),

    path('search/<str:product_title>', search, name='search'),

    path('detail/', detail, name='detail-page'),
    path('contact/', contact, name='contact-page'),
    path('checkout/', checkout, name='checkout-page'),
    path('cart/', cart, name='cart-page'),
    path('products/', include('apps.products.urls',namespace='products')),
    path('category/', category, name='category-page'),
    # ========== set language =========
    path('set-language/<str:lang>/', set_language, name='set-lang'),

    path('register/', auth_views.register_page, name='register-page'),
    path('user_register/', auth_views.user_register, name='user-register'),
    path('login_page/', auth_views.login_page, name='login-page'),
    path('user_login/', auth_views.user_login, name='user-login'),
    path('user_logout/', auth_views.user_logout, name='user-logout'),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

)
# if settings.DEBUG:
