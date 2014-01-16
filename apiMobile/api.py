from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from tastypie.resources import ModelResource, Resource, ALL, ALL_WITH_RELATIONS
from tastypie.exceptions import ImmediateHttpResponse
from tastypie import http
from mainModel.models import *
from authentication import OAuth20Authentication
from django.http.response import HttpResponse


class BaseCorsResource(Resource):
    """
    Class implementing CORS support for tastypie
    """
    def create_response(self, *args, **kwargs):
        """
        Create the response for a resource. Note this will only
        be called on a GET request, or on a POST request if 
        always_return_data is True
        """
        response = super(BaseCorsResource, self).create_response(*args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
 
    def post_list(self, request, **kwargs):
        """
        In case of POST make sure we return the Access-Control-Allow Origin
        regardless of returning data
        """
        response = super(BaseCorsResource, self).post_list(request, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Expose-Headers'] = 'Location'
        return response
        
    def method_check(self, request, allowed=None):
        """
        Check for an OPTIONS request. If so return the Allow- headers
        """
        if allowed is None:
            allowed = []
 
        request_method = request.method.lower()
        allows = ','.join(map(lambda s: s.upper(), allowed))
 
        if request_method == 'options':
            response = HttpResponse(allows)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Headers'] = 'Content-Type', 'Authorization'
            response['Access-Control-Allow-Methods'] = "GET, PUT, POST, PATCH"
            response['Allow'] = allows
            raise ImmediateHttpResponse(response=response)
 
        if not request_method in allowed:
            response = http.HttpMethodNotAllowed(allows)
            response['Allow'] = allows
            raise ImmediateHttpResponse(response=response)
 
        return request_method



class StatusReporteResource(BaseCorsResource, ModelResource):
	class Meta:
		abstract = True
		queryset = StatusReporte.objects.all()
		resource_name = 'status'
		list_allowed_methods = ['get', 'post', 'put']
		detail_allowed_methods = ['get', 'post', 'put']
		filtering = {'id':ALL,}
		authorization = DjangoAuthorization()
		authentication = OAuth20Authentication()

class StatusReporteCORSResource(StatusReporteResource):
	pass

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
		resource_name = 'oficina'
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