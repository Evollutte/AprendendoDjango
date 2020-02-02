from django.urls import path, include
from .views import index
from .views import planos, contato, duvidas

urlpatterns = [
    path('', index, name='home_blog'),
    path('post/<int:id>/', planos, name='planos'),
    path('post/<int:id>/', contato, name='contato'),
    path('post/<int:id>/', duvidas, name='duvidas'),
]
