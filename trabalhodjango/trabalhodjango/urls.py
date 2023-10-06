"""
URL configuration for trabalhodjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from projetoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista_estoque/', views.lista_estoque, name='lista_estoque'),
    path('estoque/adicionar/', views.adicionar_item_estoque, name='adicionar_item_estoque'),
    path('estoque/<int:item_id>/detalhes/', views.detalhes_item_estoque, name='detalhes_item_estoque'),
    path('estoque/<int:item_id>/editar/', views.editar_item_estoque, name='editar_item_estoque'),
    path('estoque/<int:item_id>/excluir/', views.confirmar_exclusao_item_estoque, name='confirmar_exclusao_item_estoque'),
    path('', views.lista_estoque, name='lista_estoque'),
]


