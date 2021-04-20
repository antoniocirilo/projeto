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
from ramais.views import home, infoespecifico, inicial, noticias, noticiaespecifica, adminnoticias, cadastronoticia, atualizarnoticia, deletarnoticia, aniversariantes, cadastroaniversariantes, atualizaraniversariantes, deletaraniversariantes, informativo, cadastroinformativo, atualizarinformativo,listaramais, adminramais, cadastroramal, atualizarramal, deletarramal
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('informativo/<str:mes>', infoespecifico, name="infoespecifico"),
    path('noticias/', noticias ,name="noticias"),
    path('noticias/noticia/<int:id>', noticiaespecifica, name="noticiaespecifica"),
    path('noticias/admin/', adminnoticias ,name="adminnoticias"),
    path('noticias/admin/cadastro', cadastronoticia, name="cadastronoticia"),
    path('noticias/admin/atualizar/<int:id>', atualizarnoticia, name="atualizarnoticia"),
    path('noticias/admin/deletar/<int:id>', deletarnoticia, name="deletarnoticia"),
    path('noticias/admin/aniversariante', aniversariantes, name="aniversariantes"),
    path('noticias/admin/aniversariante/cadastro', cadastroaniversariantes, name="cadastroaniversariantes"),
    path('noticias/admin/aniversariante/atualizar/<int:id>', atualizaraniversariantes, name="atualizaraniversariantes"),
    path('noticias/admin/aniversariante/deletar/<int:id>', deletaraniversariantes, name="deletaraniversariantes"),
    path('noticias/admin/informativo', informativo, name="informativo"),
    path('noticias/admin/informativo/cadastro', cadastroinformativo, name="cadastroinformativo"),
    path('noticias/admin/informativo/atualizar/<int:id>', atualizarinformativo, name="atualizarinformativo"),
    path('ramal/', inicial, name="inicial"),
    path('ramal/ramais/', listaramais, name="listaramais"),
    path('ramal/ramais/admin/', adminramais, name="adminramais"),
    path('ramal/ramais/admin/cadastro', cadastroramal, name="cadastro"),
    path('ramal/ramais/admin/atualizar/<int:id>', atualizarramal, name="atualizar"),
    path('ramal/ramais/admin/deletar/<int:id>', deletarramal, name="deletar"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
