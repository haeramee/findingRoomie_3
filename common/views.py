from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from .models import *

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request=request, username=username,password=password)
            if user is not None:
                login(request,user)
        return redirect("home")

    else:
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method =='POST':
        form=RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            new_user = form.cleaned_data.get('username')

            login(request,user)
        return redirect("login")
    else:
        form = RegisterForm()
        return render(request,'register.html',{'form':form})

def make_profile(request):
    if request.method =='POST':
        form=RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            new_user = form.cleaned_data.get('username')

            login(request,user)
        return redirect("login")
    else:
        form = RegisterForm()
        return render(request,'makeProfile.html',{'form':form})
        
# def make_profile(request,pk):
#     if request.method == 'POST':
#         # 이미지 파일 수정 안되는거 오류 해결 필요
#         form=CustomUserChangeForm(request.POST,instance=request.user,)
#         if form.is_valid():
#             form.save()
#         return redirect("MyPage")
#     else:
#         form = CustomUserChangeForm(instance = request.user)
#         return render(request,'makeProfile.html',{'form':form})
