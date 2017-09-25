from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.pedidos),
    url(r'^add/$', views.add),
    url(r'^abrir_mesa/$', views.abrir_mesa),
    url(r'^abrir_mesa1/$', views.abrir_mesa1),
    url(r'^fechar/$', views.fechar),
    url(r'^bovino/$', views.bovino),
    url(r'^frango/$', views.frango),
    url(r'^suino/$', views.suino),
    url(r'^carneiro/$', views.carneiro),
    url(r'^peixe/$', views.peixe),
    url(r'^queijo/$', views.queijo),
    url(r'^selecionaMesa/$', views.selecionaMesa),
    ]
