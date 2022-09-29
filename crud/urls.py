from django.urls import path
from . import views

app_name= "crud"
urlpatterns = [

    path('', views.home, name = "registro"),
    path('registrarmensaje', views.registrarmensaje, name = "registrar"),
    path('edicionMensaje/<nombre>', views.edicionMensaje),
    path('editarMensaje', views.editarMensaje),
    path('eliminarmensaje/<nombre>', views.eliminarmensaje),
]
