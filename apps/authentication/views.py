
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, get_user_model

from apps.authentication.forms import UserRegisterForm
from django.views import View
from django.views.generic import TemplateView

class TemplateLoginPageView(TemplateView):
    template_name = 'auth/auth-login-basic.html'


class UserLogoutView(View):

   def get(self, request, *args, **kwargs):
       logout(request)
       messages.success(request, 'You have been logged out.')
       return redirect(request.META.get('HTTP_REFERER'))


class UserLoginView(View):

    def get(self, request, *args, **kwargs):
        messages.error(request, 'Invalid email or password.')
        return redirect(settings.LOGIN_URL)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = get_user_model().objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                return redirect('home-page')
        except ObjectDoesNotExist:
            messages.error(request, 'xatolik.')
            return redirect(request.META.get('HTTP_REFERER'))


class RegisterPageView(TemplateView):
    """ this template view class open register page is
    for registering new users """
    template_name = 'auth/auth-register-basic.html'
    extra_context = {
        'forms': UserRegisterForm()
    }


class UserRegisterView(View):
    """ This View class is for registering new users """

    def get(self, request, *args, **kwargs):
        context = {
            'forms': UserRegisterForm(),
        }
        return render(request, 'auth/auth-register-basic.html', context)

    def post(self, request, *args, **kwargs):
        form_obj = UserRegisterForm(data=request.POST, )

        try:
            if form_obj.is_valid() and form_obj.cleaned_data['confirm_password'] == form_obj.cleaned_data['password']:
                form_data = form_obj.cleaned_data.copy()
                form_data.pop('confirm_password')

                messages.success(request, 'Register success')
                get_user_model().objects.get_or_create(
                    email=form_obj.cleaned_data['email'],
                    defaults={
                        'photo': form_obj.cleaned_data['photo'],
                        'first_name': form_obj.cleaned_data['first_name'],
                        'password': make_password(form_obj.cleaned_data['password']),
                    }
                )
                return redirect(settings.LOGIN_URL)

            else:
                messages.error(request, 'Passwords do not match.')
                return redirect('authentications:register-page')

        except KeyError:
            pass

        messages.error(request, form_obj.errors)
        return redirect(request.META.get('HTTP_REFERER'))
