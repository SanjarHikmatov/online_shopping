from django.urls import path
from apps.authentication import views as auth_views

app_name = 'authentications'

urlpatterns = [
    path('register/', auth_views.register_page, name='register-page'),
    path('user_register/', auth_views.user_register, name='user-register'),
    path('login_page/', auth_views.login_page, name='login-page'),
    path('user_login/', auth_views.user_login, name='user-login'),
    path('user_logout/', auth_views.user_logout, name='user-logout'),
]
