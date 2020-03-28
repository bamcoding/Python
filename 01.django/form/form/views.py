from django.shortcuts import render, redirect
from django.http import response

def write(request):
  return render(request,'write.html')
