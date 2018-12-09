from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	cedula = models.CharField(max_length=13,blank=True, default="0000000000")
	activo = models.BooleanField(default=True)
	propietario = models.BooleanField(default=True)
	dob	= models.DateField(blank=True,null=True)
	codigo_externo = models.CharField(max_length=20,blank=True,null=True)
	telefono = models.CharField(max_length=10,blank=True,default="11111111")
	movil = models.CharField(max_length=10,blank=True,default="11111111")

#User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
	if created:
		UserProfile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
	instance.userprofile.save()

	
