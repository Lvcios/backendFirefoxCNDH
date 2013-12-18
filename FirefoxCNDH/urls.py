from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from apiMobile.api import *
from tastypie.api import Api

admin.autodiscover()
#reporte_resource = ReporteResource()
v1_api = Api(api_name='v1')
v1_api.register(ReporteResource())
v1_api.register(InstitucionResource())
v1_api.register(StatusReporteResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FirefoxCNDH.views.home', name='home'),
    # url(r'^FirefoxCNDH/', include('FirefoxCNDH.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r"^$", "mainWeb.views.userIndex"),
	url(r'^api/', include(v1_api.urls)),
	url(r"^administrator/$", "administrator.views.adminIndex"),
	url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),
)

#c.client_id 'b1962fa42b0c9819c5ae'
#c.client_secret 'cf39b94a9d05350fa0c33c04b589094cca8634d6'
# curl -d "client_id=b1962fa42b0c9819c5ae&client_secret=cf39b94a9d05350fa0c33c04b589094cca8634d6&grant_type=password&username=Lvcios&password=2165584&scope=write" 127.0.0.1:8000/oauth2/access_token
#{"access_token": "02ef7977c4e707fafaadf4c039b2f343b39db3e8", "scope": "read write read+write", "expires_in": 31535999, "refresh_token": "36e24569531f5540bfc4178b019b2320abd74706"}
#curl --dump-header  -H "Content-Type: application/json" 127.0.0.1:8000/api/v1/reporte/
#curl --dump-header - -H "Authorization: OAuth 02ef7977c4e707fafaadf4c039b2f343b39db3e8" -H "Content-Type: application/json" -X POST --data  "{\"nombreInst_id\":\"/api/v1/institucion/1/\",\"nombre\":\"Lvcios\",\"apellido\":\"Malfoy\",\"correo\":\"lmalfoi@slytherin.hogwarts.uk\",\"telefono\":\"123456780\",\"descripcion\":\"El que no puede ser nombrado ha atacado de nuevo.\",\"direccion\":\"London Street 748\",\"fecha\":\"19 de Octubre 2013\",\"reincide\":true,\"status_id\":\"/api/v1/status/1/\"}" 127.0.0.1:8000/api/v1/reporte/