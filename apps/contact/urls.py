from django.urls import path

from apps.contact.views import contact_us

app_name = 'contacts'
urlpatterns = [
    path('', contact_us, name='contact-us')
]