
from django.conf.urls import url

from myapps.usuario.views import RegistroUsuario

urlpatterns = [
    url(r'^registrar$', RegistroUsuario.as_view(), name='registrar'),
   
]
