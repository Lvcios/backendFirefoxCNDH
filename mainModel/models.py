#encoding:utf-8
from django.db import models
# Create your models here.

class Institucion(models.Model):
	nombreInst = models.CharField(max_length=45, verbose_name = 'Nombre de la institucion')
	def __unicode__(self):
		return self.nombreInst
		
class StatusReporte(models.Model):
	descripcionStatus = models.CharField(max_length = 20)
	def __unicode__(self):
		return unicode(self.descripcionStatus)
	
class Reporte(models.Model):
	folio = models.AutoField(primary_key = True, verbose_name = 'Folio del reporte')
	nombreInst = models.ForeignKey(Institucion)
	nombre = models.CharField(max_length=100, verbose_name = 'Nombres')
	apellido = models.CharField(max_length=100, verbose_name = 'Apellidos ')
	correo = models.CharField(max_length=100, verbose_name = 'Correo')
	telefono = models.CharField(max_length=30, verbose_name = 'Telefono')
	descripcion = models.TextField(verbose_name = 'Descripcion de la situacion')
	direccion = models.CharField(max_length=100, verbose_name = 'Domicilio Usuario')
	fecha = models.CharField(max_length=20, verbose_name = 'Fecha del incidente') #fecha del incidente
	reincide = models.CharField(max_length=10, verbose_name = 'Situacion vivida (on off)')
	#campos automaticos
	fechaUpload = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de recibido') #fecha de guardado
	status = models.ForeignKey(StatusReporte)
	compete = models.CharField(max_length = 10, blank = True, default = "No")
	respuestaText = models.TextField(blank = True)
	cita = models.CharField(max_length = 50,blank = True)
	def __unicode__(self):
		return str(self.folio)

"""
class Oficina(models.Model):
	estado = models.CharField(max_length=50, verbose_name = 'Estado')
	data-image = models.CharField(max_length=20, verbose_name = 'url imagen')
	data-lat = models.CharField(max_length=10, verbose_name = 'latitud')
	data-lon = models.CharField(max_length=10, verbose_name = 'longitud')
	ciudad = models.CharField(max_length=100, verbose_name = 'ciudad')
	direccion = models.CharField(max_length=150, verbose_name = 'direccion')
"""