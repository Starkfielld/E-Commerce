from django.contrib import admin

# Register your models here.
from .models import Login
from .models import cliente
from .models import produto

admin.site.register(Login)
admin.site.register(cliente)
admin.site.register(produto)