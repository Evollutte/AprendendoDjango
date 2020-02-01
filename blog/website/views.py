from django.shortcuts import render
from .models import Post, Contact


def hello_blog(request):
    lista = [
        'Django', 'Python', 'Git', 'Html', 
        'Banco de dados', 'Linux', 'Nginx', 'Uwsgi',
        'Systemctl'
    ]
    list_posts = Post.objects.filter(deleted=False)

    data = {
        'name': 'Curso de Django 3', 
        'lista_tecnologias': lista, 
        'posts': list_posts }

    return render(request, 'index.html', data)

def index(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'index.html', {'post': post})

def contato(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'contato.html', {'post': post})

def duvidas(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'duvidas.html', {'post': post})

def planos(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'planos.html', {'post': post})

def save_form(request):
    name = request.POST['name']
    Contact.objects.create(
        name=name, 
        email=request.POST['email'],
        message=request.POST['message']    
    )
    return render(request, 'contact_success.html', {'name_contact': name})
