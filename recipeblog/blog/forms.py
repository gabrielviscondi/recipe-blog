from django import forms
from .models import Receita
from .models import Categoria
from .models import Tipo

class PostRecipe(forms.ModelForm):

    class Meta:
        model = Receita
        fields = ('name', 'short_desc','ingredients','instructions','hints','id_tipo','id_categoria','image')
        labels = {
            'name': 'Nome da Receita'
            ,'short_desc': 'Descrição Curta (até 50 caracteres)'
            ,'ingredients': 'Ingredientes'
            ,'instructions': 'Instruções de Preparo'
            ,'hints': 'Dicas de Preparo'
            ,'id_tipo': 'Tipo de Receita'
            ,'id_categoria': 'Categoria de Receita'
            , 'image': 'Imagem da Receita'
        }


        