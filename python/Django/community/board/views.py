from django.shortcuts import render

# Create your views here.

def boardlist(request):
    return render(request, 'boardlist.html')