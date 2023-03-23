from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST, require_safe, require_http_methods

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        # 비어있는 폼이 저기 form에 들어갈거
        form = CustomUserCreationForm()
    
    context = {'form': form,}
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        # 기존 데이터 넣어주자 -> instance 활용
        form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)