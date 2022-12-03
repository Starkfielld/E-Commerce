from django.shortcuts import render ,redirect
from django.views import View
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 


# Create your views here.

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    
class Processador(View):
    def get(self, request,*args, **kwargs):
        return render(request,'Processador.html')
class gpu(View):
    def get(self, request,*args, **kwargs):
        return render(request,'gpu.html')


def registro_request(request):
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registrado com sucesso" )
                return render(request,'index.html')
            messages.error(request, "Erro ao registrar")
        form = NewUserForm()
        return render (request=request, template_name="registro.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Você está logado como: {username}.")
				return render(request,'index.html')
			else:
				messages.error(request,"Inválido usuário or senha.")
		else:
			messages.error(request,"Inválido usuário or senha.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return render(request,'index.html')