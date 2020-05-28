from django import forms
from .models import Receita
from .models import Categoria
from .models import Tipo

class PostRecipe(forms.ModelForm):

    class Meta:
        model = Receita
        fields = ('name', 'short_desc','ingredients','instructions','hints','id_tipo','id_categoria', 'image')
