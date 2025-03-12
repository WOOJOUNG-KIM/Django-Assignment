from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login

# 회원가입 기능
def sign_up(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL) # 회원가입 후 로그인 페이지로 이동

    context = {
        'form': form,
    }
    return render(request,'registration/signup.html', context)

# 로그인 기능
def login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        django_login(request, form.get_user())
        return redirect('/todo/') # 로그인 성공시 to do 페이지로 이동

    context = {
        'form': form,
    }
    return render(request, 'registration/login.html', context)