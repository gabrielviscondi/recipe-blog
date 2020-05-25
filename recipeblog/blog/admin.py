from django.contrib import admin
from .models import Receita
from .models import Categoria
from .models import Tipo

admin.site.register(Receita)
admin.site.register(Categoria)
admin.site.register(Tipo)