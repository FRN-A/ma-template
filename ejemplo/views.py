from django.shortcuts import render

def index(request):
    return render(request, "index.html") 

def indexitem(request):
    return render(request, "indexitem.html")

def create(request):
    return render(request, 'create.html')
