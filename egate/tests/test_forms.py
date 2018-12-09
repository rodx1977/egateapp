from django.test import TestCase
from django.utils import timezone
from egate.forms import InvitacionForm,AutorizaProveedorForm,InvitadoForm
import datetime
from django.contrib.auth.models import User

class InvitacionFormTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		hoy = timezone.now()
		User.objects.create(first_name='mario',last_name='bros',email='mbros@univisa.com.ec')
		#user = User.objects.get(id=2)


	def test_fecha_invitacion_enpasado(self):
		mydate = timezone.now() - datetime.timedelta(days=1)
		user = User.objects.get(id=1)
		form_data = {'fecha_ivitacion':mydate}
		form = InvitacionForm(user,data=form_data)
		self.assertFalse(form.is_valid())

class AutorizaProveedorFormTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		hoy = timezone.now()
		User.objects.create(first_name='mario',last_name='bros',email='mbros@univisa.com.ec')

	def test_fecha_autorizacion_enpasado(self):
		#mydate = timezone.now() - datetime.timedelta(days=1)
		mydate = timezone.now() 
		user = User.objects.get(id=1)
		form_data = {'fecha_autorizacion':mydate}
		form = AutorizaProveedorForm(user,data=form_data)
		self.assertFalse(form.is_valid())

class GrabarInvitadoFormTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		hoy = timezone.now()
		User.objects.create(first_name='mario',last_name='bros',email='mbros@univisa.com.ec')

	def test_invitado_form_iscorrect(self):
		user = User.objects.get(id=1)
		cedula_data = '0000000000'
		form_data = {
			'cedula':cedula_data,
			'genero':'M',
			'email':'rodx@gmail.com',
			'telefono':'6025054',
			'movil':'0984393072',
			'pk_user':user,
			'nombres':'Rodolfo',
			'apellidos':'Rodriguez Ochoa'
		}
		form = InvitadoForm(form_data)
		self.assertTrue(form.is_valid())

	def test_invitado_form_cedula_is_zero(self):
		user = User.objects.get(id=1)
		cedula_data = '0000000000'
		form_data = {
			'cedula':cedula_data,
			'genero':'M',
			'email':'rodx@gmail.com',
			'telefono':'6025054',
			'movil':'0984393072',
			'pk_user':user,
			'nombres':'Rodolfo',
			'apellidos':'Rodriguez Ochoa'
			}
		form = InvitadoForm(form_data)
		self.assertEqual(form.fields['cedula'],'0000000000')	


