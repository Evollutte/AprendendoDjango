from django.urls import path, include
from .views import hello_blog
from .views import index, planos, contato, duvidas

urlpatterns = [
    path('', hello_blog, name='home_blog'),
    path('post/<int:id>/', index, name='index'),
    path('post/<int:id>/', planos, name='planos'),
    path('post/<int:id>/', contato, name='contato'),
    path('post/<int:id>/', duvidas, name='duvidas'),
]
