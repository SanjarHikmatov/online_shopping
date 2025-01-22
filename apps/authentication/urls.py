from django.urls import path
from apps.authentication.views import (
    RegisterPageView,
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    TemplateLoginPageView,
)

app_name = 'authentications'

urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register-page'),
    path('user_register/', UserRegisterView.as_view(), name='user-register'),
    path('login_page/', TemplateLoginPageView.as_view(), name='login-page'),
    path('user_login/', UserLoginView.as_view(), name='user-login'),
    path('user_logout/', UserLogoutView.as_view(), name='user-logout'),
]
