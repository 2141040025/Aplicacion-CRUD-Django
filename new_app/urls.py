#----------------------------------
# 		   Urls / new_app
#----------------------------------

from django.conf.urls.static import static
from django.conf.urls import include, url
#
from . import views
from relax_bro import settings

#-------------------------------------------------------------------------

urlpatterns = [
	
	# Pagina de Inicio
    url(r'^$', views.index),

    # Crear Profesor
    url(r'^profesor/crear/$', views.profesor_crear),

    # Ver Profesores
    url(r'^profesor/(?P<id>\d+)$', views.profesor_detalle),

    # Editar Profesor
    url(r'^profesor/editar/(?P<id>\d+)$', views.profesor_editar),

    # Borrar Profesor
    url(r'^profesor/borrar/(?P<id>\d+)$', views.profesor_borrar),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
