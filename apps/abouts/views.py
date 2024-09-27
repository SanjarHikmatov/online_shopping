from lib2to3.fixes.fix_input import context

from django.shortcuts import render

from apps.abouts.models import About


def about(request):
    """
    this about function
    there context use for html, it got all obj
    """
    context = {
               'abouts': About.objects.all(),
    }
    return render(request=request, template_name='about.html', context=context)