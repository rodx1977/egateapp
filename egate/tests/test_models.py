from django.test import TestCase
from egate.models import Invitacion, Invitado, Direccion,CategoriaProveedores,Proveedores,AutorizarProveedor
from django.utils import timezone
import datetime
import uuid
from django.contrib.auth.models import User


class Invitacion_test(TestCase):
	@classmethod
	def setUpTestData(cls):
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

	def test_label_fecha_emision(self):
		
		invitacion = Invitacion.objects.get(id=1)
		field_label = invitacion._meta.get_field('fecha_emision').verbose_name
		self.assertEquals(field_label,'fecha emision')

	def test_label_fecha_invitacion(self):
		
		invitacion = Invitacion.objects.get(id=1)
		field_label = invitacion._meta.get_field('fecha_invitacion').verbose_name
		self.assertEquals(field_label,'fecha invitacion')

	def test_label_estado_invitacion(self):
		
		invitacion = Invitacion.objects.get(id=1)
		field_label = invitacion._meta.get_field('estado_invitacion').verbose_name
		self.assertEquals(field_label,'estado invitacion')

	def test_max_length_estado_invitacion(self):
		invitacion = Invitacion.objects.get(id=1)
		field_length = invitacion._meta.get_field('estado_invitacion').max_length
		self.assertEquals(field_length,1)

	def test_label_nombre_invitado(self):
		
		invitacion = Invitacion.objects.get(id=1)
		field_label = invitacion._meta.get_field('nombre_invitado').verbose_name
		self.assertEquals(field_label,'nombre invitado')

	def test_label_apellido_invitado(self):
		
		invitacion = Invitacion.objects.get(id=1)
		field_label = invitacion._meta.get_field('apellido_invitado').verbose_name
		self.assertEquals(field_label,'apellido invitado')

	def test_label_cedula_invitado(self):
		
		invitacion = Invitacion.objects.get(id=1)
		field_label = invitacion._meta.get_field('cedula_invitado').verbose_name
		self.assertEquals(field_label,'cedula invitado')

	def test_label_tipo_invitacion(self):
		
		invitacion = Invitacion.objects.get(id=1)
		field_label = invitacion._meta.get_field('tipo_invitacion').verbose_name
		self.assertEquals(field_label,'tipo invitacion')

	def test_label_codigo_invitacion(self):
		
		invitacion = Invitacion.objects.get(id=1)
		field_label = invitacion._meta.get_field('codigo_invitacion').verbose_name
		self.assertEquals(field_label,'codigo invitacion')

	def test_max_length_codigo_invitacion(self):
		invitacion = Invitacion.objects.get(id=1)
		field_length = invitacion._meta.get_field('codigo_invitacion').max_length
		self.assertEquals(field_length,128)

	def test_label_cedula_invitado(self):
		
		invitacion = Invitacion.objects.get(id=1)
		field_label = invitacion._meta.get_field('cedula_invitado').verbose_name
		self.assertEquals(field_label,'cedula invitado')

	def test_max_length_cedula_invitado(self):
		invitacion = Invitacion.objects.get(id=1)
		field_length = invitacion._meta.get_field('cedula_invitado').max_length
		self.assertEquals(field_length,13)

class Invitado_test(TestCase):

	@classmethod
	def setUpTestData(cls):
		hoy = timezone.now()
		User.objects.create(first_name='mario',last_name='bros',email='mbros@univisa.com.ec')
		user = User.objects.get(id=1)
		Invitado.objects.create(
			nombres='Fidel',
			apellidos= 'Marquez',
			cedula= '0917330193',
			pk_user = user,
			)
	def test_label_nombres(self):
		invitado = Invitado.objects.get(id=1)
		field_label = invitado._meta.get_field('nombres').verbose_name
		self.assertEquals(field_label,'nombres')

	def test_label_apellidos(self):
		invitado = Invitado.objects.get(id=1)
		field_label = invitado._meta.get_field('apellidos').verbose_name
		self.assertEquals(field_label,'apellidos')

	def test_label_cedula(self):
		invitado = Invitado.objects.get(id=1)
		field_label = invitado._meta.get_field('cedula').verbose_name
		self.assertEquals(field_label,'cedula')

	def test_max_length_cedula(self):
		invitado = Invitado.objects.get(id=1)
		field_label = invitado._meta.get_field('cedula').max_length
		self.assertEquals(field_label,13)

	def test_label_genero(self):
		invitado = Invitado.objects.get(id=1)
		field_label = invitado._meta.get_field('genero').verbose_name
		self.assertEquals(field_label,'genero')

	def test_max_length_genero(self):
		invitado = Invitado.objects.get(id=1)
		field_label = invitado._meta.get_field('genero').max_length
		self.assertEquals(field_label,1)

	def test_label_email(self):
		invitado = Invitado.objects.get(id=1)
		field_label = invitado._meta.get_field('email').verbose_name
		self.assertEquals(field_label,'email')

	def test_max_length_email(self):
		invitado = Invitado.objects.get(id=1)
		field_label = invitado._meta.get_field('email').max_length
		self.assertEquals(field_label,60)

	def test_label_telefono(self):
		invitado = Invitado.objects.get(id=1)
		field_label = invitado._meta.get_field('telefono').verbose_name
		self.assertEquals(field_label,'telefono')

	def test_max_length_telefono(self):
		invitado = Invitado.objects.get(id=1)
		field_label = invitado._meta.get_field('telefono').max_length
		self.assertEquals(field_label,16)

	def test_label_movil(self):
		invitado = Invitado.objects.get(id=1)
		field_label = invitado._meta.get_field('movil').verbose_name
		self.assertEquals(field_label,'movil')

	def test_max_length_movil(self):
		invitado = Invitado.objects.get(id=1)
		field_label = invitado._meta.get_field('movil').max_length
		self.assertEquals(field_label,10)

	def test_label_pk_user(self):
		invitado = Invitado.objects.get(id=1)
		field_label = invitado._meta.get_field('pk_user').verbose_name
		self.assertEquals(field_label,'pk user')	

class Direccion_test(TestCase):

	@classmethod
	def setUpTestData(cls):
		User.objects.create(first_name='mario',last_name='bros',email='mbros@univisa.com.ec')	
		user = User.objects.get(id=1)	
		direccion = Direccion.objects.create(
			manzana = '9',
			villa = '46',
			conjunto = 'Jupiter',
			residente_pk = user,
			)


	def test_label_manzana(self):
		user = User.objects.get(id=1)
		direccion = Direccion.objects.get(id=1)
		field_label = direccion._meta.get_field('manzana').verbose_name
		self.assertEquals(field_label,'manzana')

	def test_label_villa(self):
		user = User.objects.get(id=1)
		direccion = Direccion.objects.get(id=1)
		field_label = direccion._meta.get_field('villa').verbose_name
		self.assertEquals(field_label,'villa')

	def test_label_calle1(self):
		user = User.objects.get(id=1)
		direccion = Direccion.objects.get(id=1)
		field_label = direccion._meta.get_field('calle1').verbose_name
		self.assertEquals(field_label,'calle1')

	def test_label_calle2(self):
		user = User.objects.get(id=1)
		direccion = Direccion.objects.get(id=1)
		field_label = direccion._meta.get_field('calle2').verbose_name
		self.assertEquals(field_label,'calle2')

	def test_label_conjunto(self):
		user = User.objects.get(id=1)
		direccion = Direccion.objects.get(id=1)
		field_label = direccion._meta.get_field('conjunto').verbose_name
		self.assertEquals(field_label,'conjunto')

	def test_label_departamento(self):
		user = User.objects.get(id=1)
		direccion = Direccion.objects.get(id=1)
		field_label = direccion._meta.get_field('departamento').verbose_name
		self.assertEquals(field_label,'departamento')

	def test_label_residente_pk(self):
		user = User.objects.get(id=1)
		direccion = Direccion.objects.get(id=1)
		field_label = direccion._meta.get_field('residente_pk').verbose_name
		self.assertEquals(field_label,'residente pk')

class Categoria_Proveedores_test(TestCase):
	
	@classmethod
	def setUpTestData(cls):
		CategoriaProveedores.objects.create(nombres_categoria='farmacia',estado_categoria='A')
		catprov= CategoriaProveedores.objects.get(id=1)
		

	def test_label_nombres_categoria(self):
		catprov= CategoriaProveedores.objects.get(id=1)
		field_label = catprov._meta.get_field('nombres_categoria').verbose_name
		self.assertEquals(field_label,'nombres categoria')

	def test_label_estado_categoria(self):
		catprov= CategoriaProveedores.objects.get(id=1)
		field_label = catprov._meta.get_field('estado_categoria').verbose_name
		self.assertEquals(field_label,'estado categoria')

class Proveedores_test(TestCase):
	@classmethod
	def setUpTestData(cls):
		CategoriaProveedores.objects.create(nombres_categoria='farmacia',estado_categoria='A')
		catprov= CategoriaProveedores.objects.get(id=1)
		Proveedores.objects.create(nombres_proveedor='fybeca',estado_proveedor='A',categoria_pk=catprov,direccion_proveedor='piazza villaclub',georeferencia_proveedor='0000')
		prov = Proveedores.objects.get(id=1)

	def test_label_nombres_proveedor(self):
		prov = Proveedores.objects.get(id=1)
		field_label = prov._meta.get_field('nombres_proveedor').verbose_name
		self.assertEquals(field_label,'nombres proveedor')

	def test_max_length_nombres_proveedor(self):
		prov = Proveedores.objects.get(id=1)
		field_label = prov._meta.get_field('nombres_proveedor').max_length
		self.assertEquals(field_label,100)

	def test_label_estado_proveedor(self):
		prov = Proveedores.objects.get(id=1)
		field_label = prov._meta.get_field('estado_proveedor').verbose_name
		self.assertEquals(field_label,'estado proveedor')

	def test_max_length_estado_proveedor(self):
		prov = Proveedores.objects.get(id=1)
		field_label = prov._meta.get_field('estado_proveedor').max_length
		self.assertEquals(field_label,1)

	def test_label_categoria_pk(self):
		prov = Proveedores.objects.get(id=1)
		field_label = prov._meta.get_field('categoria_pk').verbose_name
		self.assertEquals(field_label,'categoria pk')

	def test_label_direccion_proveedor(self):
		prov = Proveedores.objects.get(id=1)
		field_label = prov._meta.get_field('direccion_proveedor').verbose_name
		self.assertEquals(field_label,'direccion proveedor')

	def test_max_length_direccion_proveedor(self):
		prov = Proveedores.objects.get(id=1)
		field_label = prov._meta.get_field('direccion_proveedor').max_length
		self.assertEquals(field_label,150)

	def test_label_georeferencia_proveedor(self):
		prov = Proveedores.objects.get(id=1)
		field_label = prov._meta.get_field('georeferencia_proveedor').verbose_name
		self.assertEquals(field_label,'georeferencia proveedor')

	def test_max_length_georeferencia_proveedor(self):
		prov = Proveedores.objects.get(id=1)
		field_label = prov._meta.get_field('georeferencia_proveedor').max_length
		self.assertEquals(field_label,200)

class AutorizarProveedor_test(TestCase):
	@classmethod
	def setUpTestData(cls):
		hoy = timezone.now()
		CategoriaProveedores.objects.create(nombres_categoria='farmacia',estado_categoria='A')
		catprov= CategoriaProveedores.objects.get(id=1)
		User.objects.create(first_name='mario',last_name='bros',email='mbros@univisa.com.ec')
		Proveedores.objects.create(nombres_proveedor='fybeca',estado_proveedor='A',categoria_pk=catprov,direccion_proveedor='piazza villaclub',georeferencia_proveedor='0000')
		
		prov = Proveedores.objects.get(id=1)
		
		user = User.objects.get(id=1)
		Direccion.objects.create(
			manzana = '9',
			villa = '46',
			conjunto = 'Jupiter',
			residente_pk = user,
			)
		dir = Direccion.objects.get(id=1)
		AutorizarProveedor.objects.create(fecha_emision=hoy,fecha_autorizacion=hoy,estado_autorizacion='P',nombre_proveedor=prov,nombres_categoria=catprov,residente_pk=user,codigo_invitacion='09121212121',direccion_pk=dir)

		autprov = AutorizarProveedor.objects.get(id=1)

	def test_label_fecha_autorizacion(self):
		autprov = AutorizarProveedor.objects.get(id=1)
		field_label = autprov._meta.get_field('fecha_autorizacion').verbose_name

		self.assertEquals(field_label,'fecha autorizacion')	

	def test_label_estado_autorizacion(self):
		autprov = AutorizarProveedor.objects.get(id=1)
		field_label = autprov._meta.get_field('estado_autorizacion').verbose_name

	def test_max_length_estado_autorizacion(self):
		autprov = AutorizarProveedor.objects.get(id=1)
		field_label = autprov._meta.get_field('estado_autorizacion').max_length

		self.assertEquals(field_label,1)	

	def test_label_nombre_proveedor(self):
		autprov = AutorizarProveedor.objects.get(id=1)
		field_label = autprov._meta.get_field('nombre_proveedor').verbose_name

		self.assertEquals(field_label,'nombre proveedor')

	def test_label_residente_pk(self):
		autprov = AutorizarProveedor.objects.get(id=1)
		field_label = autprov._meta.get_field('residente_pk').verbose_name

		self.assertEquals(field_label,'residente pk')

	def test_label_codigo_invitacion(self):
		autprov = AutorizarProveedor.objects.get(id=1)
		field_label = autprov._meta.get_field('codigo_invitacion').verbose_name

		self.assertEquals(field_label,'codigo invitacion')

	def test_max_length_codigo_invitacion(self):
		autprov = AutorizarProveedor.objects.get(id=1)
		field_label = autprov._meta.get_field('codigo_invitacion').max_length

		self.assertEquals(field_label,128)

	def test_label_direccion_pk(self):
		autprov = AutorizarProveedor.objects.get(id=1)
		field_label = autprov._meta.get_field('direccion_pk').verbose_name

		self.assertEquals(field_label,'direccion pk')