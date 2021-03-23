"""Estivas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from ramais.views import listaramais, adminramais, cadastroramal, atualizarramal, deletarramal
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ramais/', listaramais, name="listaramais"),
    path('ramais/admin/', adminramais, name="adminramais"),
    path('ramais/admin/cadastro', cadastroramal, name="cadastro"),
    path('ramais/admin/atualizar/<int:id>', atualizarramal, name="atualizar"),
    path('ramais/admin/deletar/<int:id>', deletarramal, name="deletar"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
