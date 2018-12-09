from django.urls import path
from . import views


urlpatterns = [
	path('', views.update_profile, name='profile'),
	path('profileok', views.user_profile_ready, name='profile_ok'),
]