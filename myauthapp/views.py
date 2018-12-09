from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

# Create your views here.

def change_password(request):
	if request.method == "POST":
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, 'Su password ha sido exitosamente actualizado!')
			return redirect('main')
		else:
			messages.error(request,'Por favor corrija el error abajo!')
	else:
		form = PasswordChangeForm(request.user)
	return render(request,'myauthapp/change_password.html',{
		'form':form,
		})

