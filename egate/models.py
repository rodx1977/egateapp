from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#clase abstracta persona
class Person(models.Model):
	nombres = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=60)
	dob = models.DateField(blank=True,null=True)


	class Meta:
		abstract = True

class Invitado(Person):
	GENERO = (
	('M','Masculino'),
	('F','Femenino'),	
	)

	def cedula_default():
		default_cedula = '0000000000'
		return default_cedula

	cedula= models.CharField(max_length=13,blank=True, default=cedula_default)
	genero = models.CharField(max_length=1,choices=GENERO)
	email = models.EmailField(max_length=60,blank=True,null=True)
	telefono = models.CharField(max_length=16,blank=True,null=True)
	movil = models.CharField(max_length=10,blank=True,null=True)
	pk_user = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.nombres

class Direccion(models.Model):
	manzana = models.CharField(max_length=10)
	villa = models.CharField(max_length=10)
	calle1 = models.CharField(max_length=80,blank=True, null=True)
	calle2 = models.CharField(max_length=80,blank=True, null=True)
	conjunto = models.CharField(max_length=80)
	departamento = models.CharField(max_length=10,blank=True,null=True)
	residente_pk = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.manzana+" - "+self.villa

class Invitacion(models.Model):
	ESTADOS_INVITACION=(
	('Pendiente','P'),
	('Realizado','R'),
	('Cancelado','C'),
	('Vencido','V'),
	)

	TIPO_INVITACION=(
		('S','SOCIAL'),
		('T','TRABAJO'),
		)

	def cedula_default():
		default_cedula = '0000000000'
		return default_cedula

	fecha_emision = models.DateTimeField(auto_now=True)
	fecha_invitacion = models.DateTimeField()
	estado_invitacion = models.CharField(max_length=1,choices=ESTADOS_INVITACION)
	residente_pk = models.ForeignKey(User,on_delete=models.CASCADE)
	nombre_invitado = models.CharField(max_length=60)
	apellido_invitado = models.CharField(max_length=60)
	cedula_invitado = models.CharField(max_length=13, default=cedula_default,blank=True)
	tipo_invitacion = models.CharField(max_length=1,choices=TIPO_INVITACION)
	codigo_invitacion = models.CharField(max_length=128)
	save_contact = models.BooleanField(blank=True)
	direccion_pk = models.ForeignKey(Direccion,on_delete=models.CASCADE)


	def __str__(self):
		return self.nombre_invitado

class CategoriaProveedores(models.Model):
	ESTADO_PROVEEDOR=(
		('A','ACTIVO'),
		('I','INACTIVO'),
		)

	nombres_categoria = models.CharField(max_length=100)
	estado_categoria = models.CharField(max_length=1, choices=ESTADO_PROVEEDOR)

	def __str__(self):
		return self.nombres_categoria

class Proveedores(models.Model):
	ESTADO_PROVEEDOR=(
		('A','ACTIVO'),
		('I','INACTIVO'),
		)

	nombres_proveedor = models.CharField(max_length=100)
	estado_proveedor = models.CharField(max_length=1, choices=ESTADO_PROVEEDOR)
	categoria_pk = models.ForeignKey(CategoriaProveedores, on_delete=models.CASCADE)
	direccion_proveedor = models.CharField(max_length=150,blank=True,null=True)
	georeferencia_proveedor = models.CharField(max_length=200,blank=True,null=True)

	def __str__(self):
		return self.nombres_proveedor

class AutorizarProveedor(models.Model):
	ESTADOS_AUTORIZACION=(
	('Pendiente','P'),
	('Realizado','R'),
	('Cancelado','C'),
	('Vencido','V'),
	)

	fecha_emision = models.DateTimeField(auto_now=True)
	fecha_autorizacion = models.DateTimeField()
	estado_autorizacion = models.CharField(max_length=1,choices=ESTADOS_AUTORIZACION)
	nombre_proveedor = models.ForeignKey(Proveedores,on_delete=models.CASCADE)
	nombres_categoria = models.ForeignKey(CategoriaProveedores, on_delete=models.CASCADE)
	residente_pk = models.ForeignKey(User,on_delete=models.CASCADE)
	codigo_invitacion = models.CharField(max_length=128)
	direccion_pk = models.ForeignKey(Direccion,on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre_proveedor	