from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main', views.main, name='main'),
    path('invitacion', views.crearInvitacion, name='invitacion'),
    path('autorizarproveedor', views.crearAutorizacionProveedor, name='autorizarproveedor'),
    path('todayinvitations', views.todayInvitations, name='todayinvitations'),
    path('timeslotinvitations/<str:timeslot>', views.previousInvitations, name='timeslotinvitations'),
    path('timeslotnextinvitations/<str:timeslot>', views.nextInvitations, name='timeslotnextinvitations'),
    path('invitado/create', views.crearInvitado, name='crearinvitado'),
    path('direccion/create', views.crearDireccion, name='creardireccion'),
    path('ajax/load-dropdownproveedor/', views.cargarProveedores, name='ajax_cargarproveedores'),
    path('changeinvitationstate/<int:mypk>', views.setInvitationState, name='changeinvitationstate'),
]