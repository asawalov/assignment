from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import auth
from django import forms


class authform(ModelForm):
    class Meta:
        model = auth
        fields = '__all__'

# class adminuserform(ModelForm):
#     class Meta:
#         model = adminuser1
#         fields = '__all__'


# class annoymoususerform(ModelForm):
#     class Meta:
#         model = annoymoususer
#         fields = '__all__'


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


