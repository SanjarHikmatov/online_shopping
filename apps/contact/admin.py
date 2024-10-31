from django.contrib import admin
from apps.contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','user_subject', 'user_message')



