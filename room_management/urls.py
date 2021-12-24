from . import views
from django.urls import path

app_name = 'sample'

urlpatterns = [
    path('', views.start, name='home'),
    path('exit_ok', views.exit_ok, name='exit_ok'),
    path('home', views.home, name='home'),
    path('exit_confirmation', views.exit_confirmation, name='exit_confirmation'),
    path('logout_ok', views.logout_ok, name='logout_ok'),
    path('in_confirmation', views.in_confirmation, name='in_confirmation'),
    path('in_ok', views.in_ok, name='in_ok'),
    path('b302', views.in_ok, name='in_ok'),
    path('qr_reading', views.qr_reading, name='qr_reading')
]