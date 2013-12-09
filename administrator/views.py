from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def adminIndex(request):
	return render_to_response("administrator/index.html",{},RequestContext(request))