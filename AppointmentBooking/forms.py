from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].help_text=None
		self.fields['password1'].help_text=None
		self.fields['password2'].help_text=None


# class BookForm(forms.ModelForm):
# 	class Meta:
# 		model = Book
# 		fields = ('name','pdf')
