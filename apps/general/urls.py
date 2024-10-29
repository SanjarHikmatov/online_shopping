from django.urls import path
from apps.general import views

app_name = 'general'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('set-language/<str:lang>/', views.set_language, name='set-lang'),
    path('set-currency/<str:currency>/', views.set_currency, name='set-curr'),
    path('clear-session/', views.flush_session, name='clear-session'),

]
