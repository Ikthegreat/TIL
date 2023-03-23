from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.

def login(request):
    if request.method == 'POST':
        # 로그인 처리를 해줌
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')

    else:
        # 비어있는 로그인 페이지를 제공
        form = AuthenticationForm()
        
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
