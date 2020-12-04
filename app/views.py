from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate,login,logout
from .forms import UserCreateForm,AccountAuthenticationForm

def home(request):
	return render(request,'app/base.html')

def signup_view(request):
	if request.method == 'POST':
		form=UserCreateForm(request.POST)
		if form.is_valid():
			new_user=form.save()
			new_user=authenticate(phone=form.cleaned_data['phone'],password=form.cleaned_data['password1'])
			login(request,new_user)
			return redirect('home')
		else:
			print(request.POST,form.errors)
			return render(request,'app/signup.html',{'form':form})
	else:
		form=UserCreateForm()
		return render(request,'app/signup.html',{'form':form})

def logout_view(request):
	logout(request)
	return redirect('home')

def login_view(request):
	context={}
	user=request.user
	if user.is_authenticated:
		return redirect('app/base.html')
	if request.POST:
		form=AccountAuthenticationForm(request.POST)
		phone=request.POST.get('phone')
		password=request.POST.get('password')
		user=authenticate(phone=phone,password=password)
		if user:
			login(request,user)
			return redirect('home')
		else:
			context['login_form']=form
			return render(request,'app/login.html',context)
	else:
		form=AccountAuthenticationForm()
		context['login_form']=form
		return render(request,'app/login.html',context)
