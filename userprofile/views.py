from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from . import forms
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.


def user_profile_ready(request):
	return render(request,'userprofile/profileready.html')

@login_required
@transaction.atomic
def update_profile(request):
	if request.method == "POST":
		user_form = forms.UserForm(request.POST, instance=request.user)

		profile_form = forms.UserProfileForm(request.POST, instance=request.user.userprofile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save() 
			messages.success(request, 'Your profile was successfully updated!')
			return redirect('profile_ok')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		user_form = forms.UserForm(instance=request.user)
		profile_form = forms.UserProfileForm(instance=request.user.userprofile)

	return render(request,'userprofile/profile.html',{
		'user_form': user_form,
		'profile_form': profile_form,
		})