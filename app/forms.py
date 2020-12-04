from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from django.contrib.auth import authenticate

class UserCreateForm(UserCreationForm):
	class Meta:
		model=User
		fields=('name','phone','email','password1','password2')

	def __init__(self, *args, **kwargs):
		super(UserCreateForm, self).__init__(*args, **kwargs)
		for field in (self.fields['phone'],self.fields['password1'],self.fields['password2'],self.fields['name'],self.fields['email']):
			field.widget.attrs.update({'class': 'form-control '})


class AccountAuthenticationForm(forms.ModelForm):
	password=forms.CharField(label='password',widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=('phone','password')
		widgets={
		'phone':forms.TextInput(attrs={'class':'form-control'}),
		'password':forms.TextInput(attrs={'class':'fprm-control'})
		}
	def __init__(self, *args, **kwargs):
		super(AccountAuthenticationForm, self).__init__(*args, **kwargs)
		for field in (self.fields['phone'],self.fields['password']):
			field.widget.attrs.update({'class': 'form-control '})

	def clean(self):
		if self.is_valid():
			phone = self.cleaned_data.get('phone')
			password = self.cleaned_data.get('password')
			if not authenticate(phone=phone, password=password):
				raise forms.ValidationError('invalid login')


