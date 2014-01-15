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
v1_api.register(OficinaResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FirefoxCNDH.views.home', name='home'),
    # url(r'^FirefoxCNDH/', include('FirefoxCNDH.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	#url(r"^$", "mainWeb.views.loadBase"),
	url(r"^$", "mainWeb.views.userIndex"),
	url(r"^consulta/", "mainWeb.views.userConsulta"),
	url(r"^transparencia/", "mainWeb.views.userTransparencia"),
	url(r"^oficinas/", "mainWeb.views.userOficina"),
	url(r"^acercade/", "mainWeb.views.userAcercade"),
	url(r"^oficinas.json/", "mainWeb.views.getOficinas"),
	url(r'^api/', include(v1_api.urls)), #ok
	url(r"^administrator/$", "administrator.views.acceso"),
	url(r"^administrator/reportes/$", "administrator.views.adminIndex"),
	url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),
)
