from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    if request.method == 'POST':
        # 로그인 처리를 해줌
        # 로그인 포맷을 입력하고 우리에게 제출을 해준거니까
        # 데이터베이스를 조작하는 요청이니 당연히 POST로 보내야함
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            print('>>>>>>>>>>>>>>>>>>>>>>')
            auth_login(request, form.get_user())
            return redirect('articles:index')
    
    else:
        # GET으로 요청을 했다는거는
        # 맨 처음 로그인 페이지를 보려고 하는거
        # 비어있는 로그인 페이지를 제공 -> 비어있는 form 제출하면 되는거
        # context에 담아서 템플릿으로 주자
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

