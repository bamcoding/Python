from django.shortcuts import render
from django.http import HttpResponse
from user.models import User
# Create your views here.

def home(request):
  pk = request.session.get('user')
  message = {}
  if pk:
    user = User.objects.get(pk=pk)
    message['username'] = user.username
  return render(request, 'boardlist.html', message)
  # return render(request, 'boardlist.html')