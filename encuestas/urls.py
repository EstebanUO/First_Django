from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('encuesta/', views.principal, name='principal.html'),
    path('contacto/', views.contacto, name='contacto'),
    path('contacto/<str:nombre>', views.contacto, name='contacto')
]