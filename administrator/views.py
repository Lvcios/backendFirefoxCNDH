from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def adminIndex(request):
	return render_to_response("administrator/index.html",{},RequestContext(request))
	
def acceso(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			ingreso = authenticate(username = usuario, password = clave)
			if ingreso is not None:
				if ingreso.is_active:
					login(request, ingreso)
					return HttpResponse('Acceso Permitido')
				else:
					return HttpResponse('El usuario no esta activo')
			else:
				return HttpResponse('El usuario no existe')
	else:
		form = AuthenticationForm()
	return render_to_response('administrator/login.html',{'form':form}, context_instance = RequestContext(request))