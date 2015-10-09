#----------------------------------
# 		  Forms / new_app
#----------------------------------

from django import forms
#
from .models import Profesor

#-------------------------------------------------------------------------

class ProfesorForm(forms.ModelForm):
	departamento = forms.CharField(error_messages={'required': 'Este campo es obligatorio.'}, choices=TITLE_CHOICES)
	nombre = forms.CharField(error_messages={'required': 'Porfavor ingresa tu nombre.'})
	class Meta:
		model = Profesor
		fields = ['departamento', 'nombre', 'direccion', 'tel', 'imagen',]

