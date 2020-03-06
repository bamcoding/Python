from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .forms import LoginForm
import sqlite3

# Create your views here.
def logout(request):
  print('logout')
  if request.session.get('user'):
    del(request.session['user'])
  return redirect('/')

def login(request):
  if request.method=='POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      # 정상이라고 판단 null 체크만 하는듯
      request.session['user']=form.user_id
      return redirect('/')
  else:
    form = LoginForm()

  return render(request, 'login.html',{'form':form})
  # print('login')
  # message = {}
  # if request.method == 'GET':
  #   return render(request, 'login.html')
  # elif request.method == 'POST':
  #   username = request.POST.get('username',None)
  #   password = request.POST.get('password',None)

  #   if not (username and password):
  #     message['error']='모든값을 입력해주세요'
  #   else:
  #     user = User.objects.get(username=username)
  #     if not check_password(password, user.password):
  #       message['error'] = '비밀번호가 틀렸습니다.'
  #     else:
  #       request.session['user'] = user.id
  #       return redirect('/')
  # return render(request, 'login.html', message)

def register(request):
  print('Hello')
  if request.method == 'GET':
    return render(request, 'register.html')
  elif request.method == 'POST':
    username = request.POST.get('username',None)
    email = request.POST.get('email',None)
    # return HttpResponse(username)
    password = request.POST.get('password',None)
    repassword = request.POST.get('repassword',None)
    
    message = {}

    if not (username and email and password and repassword):
      message['error'] = '모든 값을 입력해주세요'
    elif password != repassword:
      message['error'] = '비밀번호가 다릅니다.'
    else:
      user = User(
          username=username,
          email=email,
          password=make_password(password)
      )
      user.save()
    return render(request, 'register.html', message)