# -*- coding: UTF-8 -*-
from django.db import models
from tastypie.utils.timezone import now
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import sys
# Create your models here.

class Institucion(models.Model):
	nombreInst = models.CharField(max_length=45, verbose_name = 'Nombre de la institucion')
	def __unicode__(self):
		return self.nombreInst
		
class StatusReporte(models.Model):
	descripcionStatus = models.CharField(max_length = 20)
	def save(self, *args, **kwargs):
		super(StatusReporte, self).save(*args, **kwargs)
		#print 'aqui se debe enviar un correo'
		reload(sys)
		sys.setdefaultencoding('latin1')
		send_mail('Test in metodo save', self.descripcionStatus, 'noreply@cndh.org',['lfloresg0801@gmail.com'], fail_silently=False)
		#print 'correo enviado'
	def __unicode__(self):
		return unicode(self.descripcionStatus) 
	
	
class Reporte(models.Model):
	folio = models.AutoField(primary_key = True, verbose_name = 'Folio del reporte')
	nombreInst = models.ForeignKey(Institucion)
	nombre = models.CharField(max_length=100, verbose_name = 'Nombres')
	apellido = models.CharField(max_length=100, verbose_name = 'Apellidos ')
	correo = models.EmailField(verbose_name = 'Correo')
	telefono = models.CharField(max_length=30, verbose_name = 'Telefono')
	descripcion = models.TextField(verbose_name = 'Descripcion de la situacion')
	direccion = models.CharField(max_length=100, verbose_name = 'Domicilio Usuario')
	fecha = models.CharField(max_length=20, verbose_name = 'Fecha del incidente') #fecha del incidente
	reincide = models.BooleanField(default = False)
	#campos automaticos
	fechaUpload = models.DateTimeField(default = now, blank  = True, verbose_name = 'Fecha de recibido') #fecha de guardado
	status = models.ForeignKey(StatusReporte, verbose_name = 'Estado del reporte')
	compete = models.CharField(max_length = 10, blank = True, default = "No")
	respuestaText = models.TextField(blank = True, verbose_name = "Respuesta")
	cita = models.CharField(max_length = 50,blank = True)
	def save(self, *args, **kwargs):
		try: 
			Reporte.objects.get(folio = self.folio)
			super(Reporte, self).save(*args, **kwargs)
		except:
			super(Reporte, self).save(*args, **kwargs)
			reload(sys)
			sys.setdefaultencoding('latin1')
			subject, from_email, to = 'Hemos recibido su reporte con folio: ' + str(self.folio) + ' - CNDH', 'noreply@cndh.org.mx', self.correo
			html_content = render_to_string('mail/templateOne.html',{'nombre':self.nombre,'apellido':self.apellido,'telefono':self.telefono,'descripcion':self.descripcion})
			msg = EmailMessage(subject, html_content, from_email, [to])
			msg.content_subtype = "html" 
			msg.send()
	def __unicode__(self):
		return str(self.folio)
		
"""
class Respuesta(models.Model):
	folio = models.ForeignKey(Reporte)
	respuestaText = models.TextField()
	fechaRespuesta = models.CharField(max_length=20, verbose_name = 'Fecha de respuesta') 
	def __unicode__(self):
		return 'Folio del reporte: ' + str(self.folio) + 'Respuesta: ' + self.respuestaText
"""
"""		
class CitaReporte(models.Model):
	reporte = models.ForeignKey(Reporte)
	cita = models.CharField(max_length = 50)
	def __unicode__(self):
		return 'El reporte ' + str(self.reporte) + 'tiene cita en la fecha ' + self.cita
"""