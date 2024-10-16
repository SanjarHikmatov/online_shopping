from django.urls import path

app_name = 'comments'

from .views import create_comment

urlpatterns = [
    path('create/', create_comment, name='create-comment'),
]
