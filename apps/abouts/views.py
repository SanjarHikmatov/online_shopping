from django.shortcuts import render

from apps.abouts.models import About

from django.views.generic import TemplateView


class TemplateAboutsView(TemplateView):
    """
     this AboutView class
     there context use for html, it got all obj
     """

    template_name = 'about.html'
    extra_context = {
        'abouts': About.objects.all()
    }
