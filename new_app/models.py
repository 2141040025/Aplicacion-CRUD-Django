#----------------------------------
# 		  Models / new_app
#----------------------------------

from django.db import models

#-------------------------------------------------------------------------

class Profesor(models.Model):
	departamento = models.ForeignKey('Departamento')
	nombre = models.CharField(max_length=200)
	direccion = models.CharField(max_length=200, blank=True)
	tel = models.CharField(max_length=30, blank=True)
	imagen = models.ImageField(upload_to='profesores/img', blank=True)

	class Meta:
		ordering = ['nombre']
		verbose_name_plural = "profesores"

	def __unicode__(self):
		return self.nombre

#-------------------------------------------------------------------------

class Departamento(models.Model):
	nombre = models.CharField(max_length=200)
	desc = models.TextField(blank=True)

	def __unicode__(self):
		return self.nombre

#-------------------------------------------------------------------------

class Curso(models.Model):
	profesor = models.ManyToManyField(Profesor)
	nombre = models.CharField(max_length=200)
	desc = models.TextField(blank=True)

	def __unicode__(self):
		return self.nombre