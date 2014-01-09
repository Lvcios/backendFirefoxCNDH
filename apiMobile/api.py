from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from mainModel.models import *
from authentication import OAuth20Authentication


class StatusReporteResource(ModelResource):
	class Meta:
		queryset = StatusReporte.objects.all()
		resource_name = 'status'
		filtering = {'id':ALL,}
		authorization = DjangoAuthorization()
		authentication = OAuth20Authentication()

class InstitucionResource(ModelResource):
	class Meta:
		queryset = Institucion.objects.all()
		resource_name = 'institucion'
		authorization = DjangoAuthorization()
		authentication = OAuth20Authentication()

class ReporteResource(ModelResource):
	nombreInst_id = fields.ForeignKey(InstitucionResource, 'nombreInst')
	status_id = fields.ForeignKey(StatusReporteResource, 'status')
	class Meta:
		queryset = Reporte.objects.all()
		resource_name = 'reporte'
		excludes = ['fechaUpload']
		filtering = {'status_id':ALL_WITH_RELATIONS,}
		always_return_data = True 
		authorization = DjangoAuthorization()
		authentication = OAuth20Authentication()
		
class OficinaResource(ModelResource):
	class Meta:
		queryset = Oficina.objects.all()
		resource_name = 'institucion'
		authorization = DjangoAuthorization()
		authentication = OAuth20Authentication()


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