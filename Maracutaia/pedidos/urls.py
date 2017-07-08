from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.pedidos),
    url(r'^addpedidos/$', views.addpedidos),
    ]
