from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class CustomerCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        # Các trường muốn hiện trên form đăng ký
        fields = ('username', 'email', 'phone', 'address')