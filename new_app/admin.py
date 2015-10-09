#----------------------------------
# 		   Admin / new_app
#----------------------------------

from django.contrib import admin
#
from .models import *

#-------------------------------------------------------------------------

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'departamento', 'direccion']
	ordering = ['nombre']

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
	pass

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
	pass