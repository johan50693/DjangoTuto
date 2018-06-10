from django.conf.urls import url

from myapps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate

urlpatterns = [
    url(r'^$', index_adopcion),
    url(r'^solicitud/listar$',SolicitudList.as_view(), name="solicitud_listar"),
    url(r'^solicitud/crear$',SolicitudCreate.as_view(), name="solicitud_crear"),
]