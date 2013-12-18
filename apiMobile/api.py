from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from mainModel.models import *


class StatusReporteResource(ModelResource):
	class Meta:
		queryset = StatusReporte.objects.all()
		resource_name = 'status'
		authorization = Authorization()
		filtering = {'id':ALL,}

class InstitucionResource(ModelResource):
	class Meta:
		queryset = Institucion.objects.all()
		resource_name = 'institucion'
		authorization = Authorization()

class ReporteResource(ModelResource):
	nombreInst_id = fields.ForeignKey(InstitucionResource, 'nombreInst')
	status_id = fields.ForeignKey(StatusReporteResource, 'status')
	class Meta:
		queryset = Reporte.objects.all()
		resource_name = 'reporte'
		excludes = ['fechaUpload']
		authorization = Authorization()
		filtering = {'status_id':ALL_WITH_RELATIONS,}
		always_return_data = True 


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
#ola k as