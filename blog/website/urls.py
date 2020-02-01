from django.urls import path, include
from .views import index, planos, contato, duvidas

urlpatterns = [
    path('', index, name='index'),
    path('', planos, name='planos'),
    path('', contato, name='contato'),
    path('', duvidas, name='duvidas'),
]
