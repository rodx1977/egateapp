from django.urls import path, re_path
from . import views
from django.contrib.auth import views as login_views


urlpatterns = [
	path('login', login_views.login, {'template_name': 'myauthapp/login.html'},name='login'),
	path('logout', login_views.logout, name='logout'),
	path('change_password', views.change_password, name='change_password'),
	path('password_reset', login_views.password_reset, {'template_name': 'myauthapp/password_reset.html','email_template_name':'myauthapp/password_reset_email.html','subject_template_name':'myauthapp/password_reset_subject.txt'},name='password_reset'),
	path('password_reset/done/', login_views.password_reset_done, {'template_name': 'myauthapp/password_reset_done.html'},name='password_reset_done'),
	re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', login_views.password_reset_confirm, {'template_name': 'myauthapp/password_reset_confirm.html'},name='password_reset_confirm'),	
	path('reset_done', login_views.password_reset_complete, {'template_name': 'myauthapp/password_reset_complete.html'},name='password_reset_complete'),
	]