from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from mainModel.models import *

class ReporteResource(ModelResource):
	class Meta:
		queryset = Reporte.objects.all()
		resource_name = 'reporte'
		excludes = ['respuestaText','cita','resource_uri']
		authorization = Authorization()
		filtering = {'folio': ALL,'nombre': ALL,'status':ALL_WITH_RELATIONS,}
		
class InstitucionResource(ModelResource):
	class Meta:
		queryset = Institucion.objects.all()
		resource_name = 'institucion'
		authorization = Authorization()
		
class StatusReporteResource(ModelResource):
	class Meta:
		queryset = StatusReporte.objects.all()
		resource_name = 'status'
		authorization = Authorization()



#codigo de ejemplo:
"""
from tastypie.resources import ModelResource
from mainModel.models import *
# Create you api here.

class ReporteResource(ModelResource):
	class Meta:
		queryset = Reporte.objects.all()
		resource_name = 'reporte'
		excludes = ['respuestaText','cita','meta']
"""
#tastypie rules!