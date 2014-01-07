from django.db.models.signals import post_save
from mainModel.models import *
 
def send_update(**kwargs):
	print 'enviar email'
	
post_save(send_update, sender = StatusReporte)