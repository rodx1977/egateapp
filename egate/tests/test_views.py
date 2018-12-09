from django.test import TestCase
from egate.models import Invitacion, Invitado, AutorizarProveedor, Direccion,CategoriaProveedores,Proveedores
from django.utils import timezone
import datetime
import uuid
from django.contrib.auth.models import User
from django.urls import reverse

class VerInvitacionListTodayTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		test_user1 = User.objects.create_user(username='testuser1', password='12345')
		myId = uuid.uuid1()
		hoy = timezone.now()
		User.objects.create(first_name='mario',last_name='bros',email='mbros@univisa.com.ec')
		user= User.objects.get(id=1)
		Direccion.objects.create(manzana='5',villa='12',conjunto='Jupiter',residente_pk=user)
		direccion = Direccion.objects.get(id=1)
		Invitacion.objects.create(
			fecha_emision = hoy,
			fecha_invitacion = hoy,
			estado_invitacion = 'P',
			residente_pk = user ,
			nombre_invitado = 'Gilmar',
			apellido_invitado = 'Gutierrez',
			cedula_invitado = '0917330193',
			tipo_invitacion = 'S',
			codigo_invitacion = myId,
			save_contact = False,
			direccion_pk = direccion,
			)
	def test_invitacion_content(self):
		invitacion  = Invitacion.objects.get(id=1)
		expected_object_name = f'{invitacion.nombre_invitado}'
		self.assertEquals(expected_object_name,'Gilmar')

	def test_redirect_if_not_loggedin(self):
		resp = self.client.get(reverse('todayinvitations'))
		self.assertRedirects(resp,'/myauth/login?next=/egate/todayinvitations')

	def test_logged_in_uses_correct_template(self):
	 	login = self.client.login(username='testuser1', password='12345')
	 	resp = self.client.get(reverse('todayinvitations'))
	 	#Check our user is logged in
	 	self.assertEqual(str(resp.context['user']), 'testuser1')
	 	self.assertEqual(resp.status_code, 200)

	 	self.assertTemplateUsed(resp, 'egate/view_invitations.html')

class VerInvitacionListPastTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		test_user1 = User.objects.create_user(username='testuser1', password='12345')
		myId = uuid.uuid1()
		hoy = timezone.now()
		User.objects.create(first_name='mario',last_name='bros',email='mbros@univisa.com.ec')
		user= User.objects.get(id=1)
		Direccion.objects.create(manzana='5',villa='12',conjunto='Jupiter',residente_pk=user)
		direccion = Direccion.objects.get(id=1)
		Invitacion.objects.create(
			fecha_emision = hoy,
			fecha_invitacion = hoy - datetime.timedelta(days=5),
			estado_invitacion = 'P',
			residente_pk = user ,
			nombre_invitado = 'Gilmar',
			apellido_invitado = 'Gutierrez',
			cedula_invitado = '0917330193',
			tipo_invitacion = 'S',
			codigo_invitacion = myId,
			save_contact = False,
			direccion_pk = direccion,
			)
	def test_invitacion_content(self):
		invitacion  = Invitacion.objects.get(id=1)
		expected_object_name = f'{invitacion.nombre_invitado}'
		self.assertEquals(expected_object_name,'Gilmar')

	def test_redirect_if_not_loggedin(self):
		resp = self.client.get(reverse('timeslotinvitations',args=('lastweek',)))
		self.assertRedirects(resp,'/myauth/login?next=/egate/timeslotinvitations/lastweek')


	def test_view_data_in_thepast(self):
		invitacion  = Invitacion.objects.get(id=1)
		hoy = timezone.now()
		fecha_test = invitacion.fecha_invitacion
		delta = hoy - fecha_test
		self.assertTrue(delta.days > 0)

class VerInvitacionListFutureTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		test_user1 = User.objects.create_user(username='testuser1', password='12345')
		myId = uuid.uuid1()
		hoy = timezone.now()
		User.objects.create(first_name='mario',last_name='bros',email='mbros@univisa.com.ec')
		user= User.objects.get(id=1)
		Direccion.objects.create(manzana='5',villa='12',conjunto='Jupiter',residente_pk=user)
		direccion = Direccion.objects.get(id=1)
		Invitacion.objects.create(
			fecha_emision = hoy,
			fecha_invitacion = hoy + datetime.timedelta(days=5),
			estado_invitacion = 'P',
			residente_pk = user ,
			nombre_invitado = 'Gilmar',
			apellido_invitado = 'Gutierrez',
			cedula_invitado = '0917330193',
			tipo_invitacion = 'S',
			codigo_invitacion = myId,
			save_contact = False,
			direccion_pk = direccion,
			)
	def test_invitacion_content(self):
		invitacion  = Invitacion.objects.get(id=1)
		expected_object_name = f'{invitacion.nombre_invitado}'
		self.assertEquals(expected_object_name,'Gilmar')

	def test_redirect_if_not_loggedin(self):
		resp = self.client.get(reverse('timeslotnextinvitations',args=('thisweek',)))
		self.assertRedirects(resp,'/myauth/login?next=/egate/timeslotnextinvitations/thisweek')


	def test_view_data_in_thefuture(self):
		invitacion  = Invitacion.objects.get(id=1)
		hoy = timezone.now()
		fecha_test = invitacion.fecha_invitacion
		delta = hoy - fecha_test
		self.assertTrue(delta.days < 0)

class AutorizarProveedorTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		test_user1 = User.objects.create_user(username='testuser1', password='12345')
		myId = uuid.uuid1()
		hoy = timezone.now()
		User.objects.create(first_name='mario',last_name='bros',email='mbros@univisa.com.ec')
		user= User.objects.get(id=1)
		Direccion.objects.create(manzana='5',villa='12',conjunto='Jupiter',residente_pk=user)
		direccion = Direccion.objects.get(id=1)
		CategoriaProveedores.objects.create(nombres_categoria='farmacia',estado_categoria='A')
		catprov= CategoriaProveedores.objects.get(id=1)
		Proveedores.objects.create(nombres_proveedor='fybeca',estado_proveedor='A',categoria_pk=catprov,direccion_proveedor='piazza villaclub',georeferencia_proveedor='0000')
		prov = Proveedores.objects.get(id=1)
		AutorizarProveedor.objects.create(fecha_emision=hoy,fecha_autorizacion=hoy,estado_autorizacion='P',nombre_proveedor=prov,nombres_categoria=catprov,residente_pk=user,codigo_invitacion='09121212121',direccion_pk=direccion)

	def test_autorizar_proveedor_content(self):
		autorizacion  = AutorizarProveedor.objects.get(id=1)
		expected_object_name = f'{autorizacion.nombre_proveedor}'
		self.assertEquals(expected_object_name,'fybeca') 

	def test_redirect_if_not_loggedin(self):
		resp = self.client.get(reverse('autorizarproveedor'))
		self.assertRedirects(resp,'/myauth/login?next=/egate/autorizarproveedor')

	def test_logged_in_uses_correct_template(self):
	 	login = self.client.login(username='testuser1', password='12345')
	 	resp = self.client.get(reverse('autorizarproveedor'))
	 	#Check our user is logged in
	 	self.assertEqual(str(resp.context['user']), 'testuser1')
	 	self.assertEqual(resp.status_code, 200)

	 	self.assertTemplateUsed(resp, 'egate/autorizaproveedorform.html')

class MakeInvitationsTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		test_user1 = User.objects.create_user(username='testuser1', password='12345')
		myId = uuid.uuid1()
		hoy = timezone.now()
		User.objects.create(first_name='mario',last_name='bros',email='mbros@univisa.com.ec')
		user= User.objects.get(id=1)
		Direccion.objects.create(manzana='5',villa='12',conjunto='Jupiter',residente_pk=user)
		direccion = Direccion.objects.get(id=1)
		Invitacion.objects.create(
			fecha_emision = hoy,
			fecha_invitacion = hoy,
			estado_invitacion = 'P',
			residente_pk = user ,
			nombre_invitado = 'Gilmar',
			apellido_invitado = 'Gutierrez',
			cedula_invitado = '0917330193',
			tipo_invitacion = 'S',
			codigo_invitacion = myId,
			save_contact = False,
			direccion_pk = direccion,
			)

	# def test_view_url_exists_at_desired_location(self):
	# 	resp = self.client.get('/egate/invitacion',follow=True)
		
	# 	self.assertEqual(resp.status_code,200)

	def test_invitacion_content(self):
		invitacion  = Invitacion.objects.get(id=1)
		expected_object_name = f'{invitacion.nombre_invitado}'
		self.assertEquals(expected_object_name,'Gilmar') 

	# def test_invitacion_list_view(self):
	#  	response = self.client.get(reverse('invitacion'),follow=True)
	#  	self.assertEqual(response.status_code,200)

	def test_redirect_if_not_loggedin(self):
		resp = self.client.get(reverse('invitacion'))
		self.assertRedirects(resp,'/myauth/login?next=/egate/invitacion')

	#test for login feature when getting the make invitation
	def test_logged_in_uses_correct_template(self):
	 	login = self.client.login(username='testuser1', password='12345')
	 	resp = self.client.get(reverse('invitacion'))
	 	#Check our user is logged in
	 	self.assertEqual(str(resp.context['user']), 'testuser1')
	 	self.assertEqual(resp.status_code, 200)

	 	self.assertTemplateUsed(resp, 'egate/invitacionform.html')