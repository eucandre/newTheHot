from django.conf.urls import url
from django.contrib import admin
from app_usuario.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',apresentacao),
    url(r'^admin/', admin.site.urls),
    url(r'^cadastro',cria_cliente),
    url(r'^criaanuncio',criaanuncio),
    url(r'^sala/$',sala_show),
    url(r'^recebe_room/$',sala_receive),
    url(r'^cam-girls/$', cam_girls, name='cam-girls'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
