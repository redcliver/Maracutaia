from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.mesas),
    url(r'^detalhe/$', views.detalhe),
    ]
