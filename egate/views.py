import pytz
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models, forms
import datetime
import uuid
from django.utils import timezone
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
   # return HttpResponse("Hello, world. You're at the egate index.")

   return render(request,'egate/index.html')

@login_required(login_url='login')
def main(request):
	return render(request,'egate/main.html')

@login_required(login_url='login')
def todayInvitations(request):
	today_list = models.Invitacion.objects.filter(fecha_invitacion__date=datetime.date.today(), residente_pk=request.user)
	today_list_provider = models.AutorizarProveedor.objects.filter(fecha_autorizacion__date=datetime.date.today(),residente_pk=request.user)
	#today_list = models.Invitacion.objects.all()
	context = {'invitation_list': today_list, 'autorizacion_list':today_list_provider}
	return render(request,'egate/view_invitations.html',context)

@login_required(login_url='login')
def nextInvitations(request,timeslot):

	if timeslot == "thisweek":
		d = 7
	days_forward = datetime.date.today() + timedelta(days=d)
	start_date = datetime.date.today()
	if d == 7:
		week_list = models.Invitacion.objects.filter(residente_pk=request.user).exclude(fecha_invitacion__lt=datetime.date.today()).filter(fecha_invitacion__range=(start_date,days_forward))
		week_list_provider = models.AutorizarProveedor.objects.filter(residente_pk=request.user).exclude(fecha_autorizacion__lt=datetime.date.today()).filter(fecha_autorizacion__range=(start_date,days_forward))
	context = {'invitation_list':week_list, 'autorizacion_list':week_list_provider}
	return render(request,'egate/view_invitations.html',context)

@login_required(login_url='login')
def previousInvitations(request,timeslot):
	d=0
	
	if timeslot == "lastweek":
		d= 7
	if timeslot == "lastmonth":
		d= 30
	if timeslot == "all":
		d= 0
	
	days_ago = datetime.date.today() - timedelta(days=d)
	start_date = datetime.date.today()

	if d == 0:
		week_list = models.Invitacion.objects.filter(residente_pk=request.user)	
		week_list_provider = models.AutorizarProveedor.objects.filter(residente_pk=request.user)	

	else:
		week_list = models.Invitacion.objects.filter(residente_pk=request.user).exclude(fecha_invitacion__gt=datetime.date.today()).filter(fecha_invitacion__range=(days_ago,start_date))
		week_list_provider = models.AutorizarProveedor.objects.filter(residente_pk=request.user).exclude(fecha_autorizacion__gt=datetime.date.today()).filter(fecha_autorizacion__range=(days_ago,start_date))
	context = {'invitation_list':week_list, 'autorizacion_list':week_list_provider}
	return render(request,'egate/view_invitations.html',context)

@login_required(login_url='login')
def crearAutorizacionProveedor(request):
	if request.method == "POST":
		form = forms.AutorizaProveedorForm(request.user,data=request.POST)
		if form.is_valid():
			prev_form = form.save(commit=False)
			now = timezone.now()
			prev_form.fecha_emision = now
			prev_form.estado_autorizacion = 'P'
			myId = uuid.uuid1()
			prev_form.codigo_invitacion = myId.hex
			prev_form.residente_pk = request.user
			prev_form.save()
			return redirect('todayinvitations')

	else:
		#se valida que antes de generar una invitacion el cliente tenga dato de su direccion
		try:
			tieneDireccion = models.Direccion.objects.filter(residente_pk=request.user.id)
		except models.Direccion.DoesNotExist:
			tieneDireccion = None
		if not tieneDireccion:
			return redirect('creardireccion')
		direcciondata = tieneDireccion
		direccionpk = direcciondata[0].id
		logger.debug('el id de direccion es ' + str(direcciondata[0].id))

		form = forms.AutorizaProveedorForm(request.user)
	return render(request,'egate/autorizaproveedorform.html',{'form':form})	

#view para obtener solamente los proveedores que la categoria seleccionada entreguen
def cargarProveedores(request):
	categoria_id = request.GET.get('nombres_categoria')
	proveedores = models.Proveedores.objects.filter(categoria_pk = categoria_id).order_by('nombres_proveedor')
	return render(request,'egate/dropdownproveedores.html',{'proveedores':proveedores})

@login_required(login_url='login')
def crearInvitacion(request):
	if request.method =="POST":	
		form = forms.InvitacionForm(request.user,data=request.POST)
		if form.is_valid():
			prev_form = form.save(commit=False)
			# now = datetime.datetime.now(tz=timezone.utc)
			now = timezone.now()
			prev_form.fecha_emision = now
			prev_form.estado_invitacion = 'P'
			myId = uuid.uuid1()
			prev_form.codigo_invitacion = myId.hex
			prev_form.residente_pk = request.user
			prev_form.save()
			#si se marco el visto de grabar se guarda un contacto
			if prev_form.save_contact:
				myform = request.POST.copy()
				models.Invitado.objects.create(
					nombres = myform.get('nombre_invitado'),
					apellidos = myform.get('apellido_invitado'),
					cedula = myform.get('cedula_invitado'),
					pk_user = request.user
					)
			return redirect('todayinvitations')
		else:
			messages.error(request,"Por favor revise las observaciones indicadas abajo")
	else:
		#se valida que antes de generar una invitacion el cliente tenga dato de su direccion
		try:
			tieneDireccion = models.Direccion.objects.filter(residente_pk=request.user.id)
		except models.Direccion.DoesNotExist:
			tieneDireccion = None
		if not tieneDireccion:
			return redirect('creardireccion')
		#fdv
		direcciondata = tieneDireccion
		direccionpk = direcciondata[0].id
		logger.debug('el id de direccion es ' + str(direcciondata[0].id))
		
		form = forms.InvitacionForm(request.user)

	return render(request,'egate/invitacionform.html',{'form':form})

@login_required(login_url='login')
def crearDireccion(request):
	if request.method == "POST":
		form = forms.DireccionForm(request.POST, request.user)
		if form.is_valid():
			prev_form = form.save(commit=False)
			prev_form.residente_pk = request.user
			prev_form.save()
			return redirect('main')
	else:
		form = forms.DireccionForm(instance=request.user)
	return render(request,'egate/direccionform.html',{'form':form})

@login_required(login_url='login')
def crearInvitado(request):
	if request.method == "POST":
		form = forms.InvitadoForm(request.POST, request.user)
		if form.is_valid():
			prev_form = form.save(commit=False)
			prev_form.pk_user = request.user
			prev_form.save()
			return redirect('main')
		else:
			messages.error(request,"Por favor revise las observaciones indicadas abajo")
	else:
		form = forms.InvitadoForm(instance=request.user)

	return render(request, 'egate/invitadoform.html',{'form':form})

@login_required(login_url='login')
def setInvitationState(request,mypk):
	if request.method == "GET":
		invitation_element = models.Invitacion.objects.get(pk=mypk)
		invitation_element.estado_invitacion = 'C'
		invitation_element.save()
	return redirect('todayinvitations')

