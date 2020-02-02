from django.shortcuts import render
from .models import Post, Contact


def index(request):
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

def contato(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'contato.html', {'post': post})

def duvidas(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'duvidas.html', {'post': post})

def planos(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'planos.html', {'post': post})