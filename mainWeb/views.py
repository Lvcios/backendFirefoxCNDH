from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def userIndex(request):
	return render_to_response("mainWeb/formulario.html",{},RequestContext(request))
	
def userConsulta(request):
	return render_to_response("mainWeb/consultar.html",{},RequestContext(request))
	
def userTransparencia(request):
	return render_to_response("mainWeb/transparencia.html",{},RequestContext(request))

def userAcercade(request):
	return render_to_response("mainWeb/acercade.html",{},RequestContext(request))
	
def getOficinas(request):
	response = render_to_response("mainWeb/oficinas.json",{},RequestContext(request))
	response["Access-Control-Allow-Origin"] = "*" 
	return response