from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.outros),
    url(r'^addespeto/$', views.addespeto),
    url(r'^editespetos/$', views.editespetos),
    url(r'^editespetos1/$', views.editespetos1),
    url(r'^addbebida/$', views.addbebida),
    url(r'^editbebidas/$', views.editbebidas),
    url(r'^editbebidas1/$', views.editbebidas1),
    url(r'^addporcao/$', views.addprocao),
    url(r'^editporcao/$', views.editporcao),
    url(r'^editporcao1/$', views.editporcao1),
    url(r'^addsobremesa/$', views.addsobremesa),
    url(r'^editsobremesa/$', views.editsobremesa),
    url(r'^editsobremesa1/$', views.editsobremesa1),
    url(r'^addacomp/$', views.addacomp),
    url(r'^editacomp/$', views.editacomp),
    url(r'^editacomp1/$', views.editacomp1),
    ]
