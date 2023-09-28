from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm,SignInForm


# Create your views here.
def home(request):
  if request.method=='POST':
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user)
      messages.success(request," login success " )
      return redirect('home')
    else:
      messages.success(request,"there was an error please try again!!")
      return redirect('home')
  else:
    form=SignInForm()
    context={
      'form':form,
    
    }
    return render(request,'home.html',context)
  

def logout_user(request):
  logout(request)
  messages.info(request," logout success ")

  return redirect('home')

def register_user(request):
  if request.method=='POST':
    form=SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username=form.cleaned_data['username']
      password=form.cleaned_data['password1']
      user=authenticate(request,username=username,password=password)
      login(request,user)
      messages.info(request,'welcome')
      return redirect('home')
  else:
    form=SignUpForm()
    return render(request,'register.html',{'form':form})
      