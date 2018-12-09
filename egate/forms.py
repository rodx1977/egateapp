from datetime import datetime,date
import logging
from django import forms
from django.forms import ModelForm, Form
from .models import Invitacion,Invitado, Direccion, AutorizarProveedor, CategoriaProveedores,Proveedores
from django.core.exceptions import ValidationError
from django.utils import timezone
import pytz


logger = logging.getLogger(__name__)

class AutorizaProveedorForm(ModelForm):
	
	
	class Meta:
		model= AutorizarProveedor
		fields = ['fecha_autorizacion','nombres_categoria','nombre_proveedor','direccion_pk']

	def __init__(self,user,*args,**kwargs):
		
		super(AutorizaProveedorForm,self).__init__(*args,**kwargs)
		self.fields['direccion_pk'].queryset = Direccion.objects.filter(residente_pk=user)
		self.fields['nombre_proveedor'].queryset = Proveedores.objects.none()

		if 'nombres_categoria' in self.data:
			categoriaid = int(self.data.get('nombres_categoria'))
			self.fields['nombre_proveedor'].queryset = Proveedores.objects.filter(categoria_pk=categoriaid).order_by('nombres_proveedor')	


	def clean_fecha_autorizacion(self):
		data = self.cleaned_data['fecha_autorizacion']
		#se verifica que la fecha de invitacion no este en el pasado
		utc = pytz.UTC
		now = utc.localize(datetime.today())
		#data = utc.localize(data)
		td = now - data
		logger.debug('data es '+ str(data))
		logger.debug('now es  '+ str(now))
		logger.debug('la resta es '+ str(td))
		if data.date() < now.date():
			logger.debug('entro al if de la fecha menor')
			raise ValidationError('Fecha no valida, ya que se encuentra en el pasado')
		#se retorna la data al caller	
		return data
	


class InvitacionForm(ModelForm):
	# guardar_invitado = forms.BooleanField(required=False)
	
	
	class Meta:
		model = Invitacion
		fields = ['fecha_invitacion','nombre_invitado','apellido_invitado','cedula_invitado','tipo_invitacion','save_contact','direccion_pk']
		labels = {
			'save_contact': 'Guardar Contacto',
		}
		help_texts = {
			'save_contact':'Da Clic si deseas que este Invitado se guarde en tu Libreta de Contactos.',
		}
	def __init__(self,user,*args,**kwargs):
		
		super(InvitacionForm,self).__init__(*args,**kwargs)
		self.fields['direccion_pk'].queryset = Direccion.objects.filter(residente_pk=user)


	def clean_fecha_invitacion(self):
		data = self.cleaned_data['fecha_invitacion']
		#se verifica que la fecha de invitacion no este en el pasado
		utc = pytz.UTC
		now = utc.localize(datetime.today())
		#data = utc.localize(data)
		td = now - data
		logger.debug('data es '+ str(data))
		logger.debug('now es  '+ str(now))
		logger.debug('la resta es '+ str(td))
		if data.date() < now.date():
			logger.debug('entro al if de la fecha menor')
			raise ValidationError('Fecha no valida, ya que se encuentra en el pasado')

		#se retorna la data al caller	
		return data

class InvitadoForm(ModelForm):
	class Meta:
		model = Invitado
		fields = ['nombres','apellidos','cedula','genero','email','telefono','movil']

	# def clean_dob(self):
	# 	data = self.cleaned_data['dob']
	# 	now = timezone.now()
	# 	if data > now:
	# 		logger.debug('fecha de nacimiento esta en el futuro')
	# 		raise ValidationError('Fecha de Nacimiento invalida, pues esta en el futuro')

	# 	return data

class DireccionForm(ModelForm):
	class Meta:
		model = Direccion
		fields = ['manzana','villa']
		labels = {
			'manzana':'Manzana',
			'villa':'Villa',
		}