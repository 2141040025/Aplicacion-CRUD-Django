#----------------------------------
# 		   Views / new_app
#----------------------------------

from django.shortcuts import render, get_object_or_404, redirect
#
from .models import *
from .forms import *

#-------------------------------------------------------------------------

def index(request):  # Profesor Lista.
	profesores = Profesor.objects.all()

	context = {
		"profesores": profesores,
	}

	return render(request, "index.html", context)

#-------------------------------------------------------------------------

def profesor_detalle(request, id):  # Profesor Ver.
	profesor = get_object_or_404(Profesor, id=id)

	context = {
		"profesor": profesor,
	}

	return render(request, "profesor_detalle.html", context)

#-------------------------------------------------------------------------

def profesor_borrar(request, id,):  # Profesor Borrar

	profesor = get_object_or_404(Profesor, id=id)

	if request.method == 'POST':
		profesor.delete()
		return redirect('/')

	context = {
		"profesor": profesor,
	}

	return render(request, "confirm_delete.html", context)

#-------------------------------------------------------------------------

def profesor_crear(request):  # Profesor Crear.

	form = ProfesorForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('/')

	context = {
		"form": form,
	}

	return render(request, "profesor_form.html", context)

#-------------------------------------------------------------------------

def profesor_editar(request, id):  # Profesor Editar

	profesor = get_object_or_404(Profesor, id=id)
	form = ProfesorForm(request.POST or None, instance=profesor)
 	# form = bookformset(request.POST, request.FILES, instance=a)
 	
	if form.is_valid():
		form.save()
		return redirect('/')

	context = {
		"form": form,
	}

	return render(request, "profesor_form.html", context)




















