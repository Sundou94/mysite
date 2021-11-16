from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import UserForm

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) #앞에서 받은 username, password를 받아서 인증정보를 authenticate을 통해 인증체크를 해줌
            login(request, user) #그 체크한게 문제가 없으면 자동로그인을 해줌
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form':form})
