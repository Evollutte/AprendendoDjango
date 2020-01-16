from django.shortcuts import render

def hello_blog(request):
    data = {'nome'}
    return render(request, 'index.html')
