from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from user.models import User
from .models import Board
from .forms import BoardForm
# Create your views here.

def home(request):
  message = {}
  boards = Board.objects.all().order_by('-id')
  pageNo = int(request.GET.get('p', 1))
  paginator = Paginator(boards, 2)#한 페이지당 몇 개씩

  boards = paginator.get_page(pageNo)
  message['boards'] = boards
  try:
    pk = request.session.get('user')
    user = User.objects.get(pk=pk)
    message['username'] = user.username
  except User.DoesNotExist:
    pass

  return render(request, 'list.html', message)

def write(request):
  message = {}
  try:
    pk = request.session.get('user')
    user = User.objects.get(pk=pk)
    message['username']= user.username
  except User.DoesNotExist:
    return redirect('/user/login')
  
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
  
  message['form']=form
  return render(request, 'write.html', message)

def detail(request, bpk):
  message = {}
  try:
    upk = request.session.get('user')
    user = User.objects.get(pk=upk)
    message['user']=user
  except User.DoesNotExist:
    pass

  try:
    board = Board.objects.get(pk=bpk)
    message['board']=board
    return render(request, 'detail.html', message) 
  except Board.DoesNotExist:
    raise Http404('게시글을 찾을 수 없습니다.')