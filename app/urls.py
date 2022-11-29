from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view()),
    path('Processador',Processador.as_view()),
    path('registro',registro_request),
    path("login",login_request),
    path('gpu',gpu.as_view())
]   
