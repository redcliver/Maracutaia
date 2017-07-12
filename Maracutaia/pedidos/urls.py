from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.pedidos),
    url(r'^add/$', views.add),
    url(r'^abrir/$', views.abrir),
    url(r'^fechar/$', views.fechar),
    url(r'^selecionaMesa/$', views.selecionaMesa),
    ]
