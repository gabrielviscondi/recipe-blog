from django.db.models import Q
import django_filters
from .models import Receita, Tipo, Categoria

class BuscaFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='busca_nome_ingrediente', label="Nome ou ingrediente")
    class Meta:
        model = Receita
        fields = ['q', 'id_tipo',  'id_categoria']

    def busca_nome_ingrediente(self, queryset, name, value):
        if bool(value and not value.isspace()):
            return queryset.filter(
            Q(name__icontains=value) |
            Q(ingredients__icontains=value))

    def __init__(self, *args, **kwargs):
       super(BuscaFilter, self).__init__(*args, **kwargs)
       self.filters['id_tipo'].label="Tipo da Receita"
       self.filters['id_categoria'].label="Categoria da Receita"