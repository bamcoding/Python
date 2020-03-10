from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import User
from .models import Board
from .forms import BoardForm
# Create your views here.

def home(request):
  boards = Board.objects.all().order_by('-id')
  pk = request.session.get('user')
  message = {}
  message['boards'] = boards
  if pk:
    user = User.objects.get(pk=pk)
    message['username'] = user.username
  return render(request, 'boardlist.html', message)

def boardwrite(request):
  pk = request.session.get('user')
  user = User.objects.get(pk=pk)
  form = BoardForm()
  if request.method == 'POST':
    form = BoardForm(request.POST)
    if form.is_valid():
      board = Board()
      board.title = form.cleaned_data['title']
      board.description = form.cleaned_data['description']
      board.writer = user
      board.save()
      return redirect('/')
  
  message = {'form':form}
  message['username']= user.username
  return render(request, 'boardwrite.html', message)