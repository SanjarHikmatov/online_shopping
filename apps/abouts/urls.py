from django.urls import path

from apps.abouts.views import TemplateAboutsView
app_name = 'about'

urlpatterns = [
    path('', TemplateAboutsView.as_view(), name='about-page'),
]