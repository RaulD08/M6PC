from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('vehiculo/add/', vehiculo_add, name='vehiculo_add'),
    path('register/', registro_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('vehiculo/list/', vehiculo_list, name='vehiculo_list'),
    path('403/', no_permiso, name='403'),

]