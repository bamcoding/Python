from django.shortcuts import render

# Create your views here.
def register(request):
    v = {}
    return render(request, 'register.html', v)