from django.shortcuts import render
from django.utils import timezone
from .models import Receita

def post_list(request):
    receitas = Receita.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'receitas': receitas})

def generic(request, id):
    receita = Receita.objects.get(pk=id)
    return render(request, 'blog/generic.html', {'receita': receita})