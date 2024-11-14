from django import forms

from apps.orders.models import Order
from apps.users.models import CustomUser


class OrdersForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=CustomUser.objects.all(), required=False, widget=forms.HiddenInput())
    class Meta:
        model = Order
        fields = '__all__'

