from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def getOficinas(request):
	response = render_to_response('mainWeb/oficinas.json',{},RequestContext(request))
	response["Access-Control-Allow-Origin"] = "*" 
	return response 
	