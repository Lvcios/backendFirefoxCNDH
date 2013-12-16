from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from mainModel.models import *


class StatusReporteResource(ModelResource):
	class Meta:
		queryset = StatusReporte.objects.all()
		resource_name = 'status'
		authorization = Authorization()

class InstitucionResource(ModelResource):
	class Meta:
		queryset = Institucion.objects.all()
		resource_name = 'institucion'
		authorization = Authorization()

class ReporteResource(ModelResource):
	nombreInst_id = fields.ForeignKey(InstitucionResource, 'nombreInst')
	#status_id = fields.ForeignKey(StatusReporteResource, 'descripcionStatus')
	status_id = fields.ForeignKey(StatusReporteResource, 'status')
	class Meta:
		queryset = Reporte.objects.all()
		resource_name = 'reporte'
		excludes = ['respuestaText','cita','resource_uri','fechaUpload']
		authorization = Authorization()
		filtering = {'folio': ALL,'nombre': ALL,'status':ALL_WITH_RELATIONS,}


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