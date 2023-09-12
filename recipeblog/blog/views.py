from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Receita
from .models import Categoria
from .forms import PostRecipe
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .filters import BuscaFilter


def home_page(request):
    receitas = Receita.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:9]
    return render(request, 'blog/home_page.html', {'receitas': receitas})

def generic(request, id):
    receita = Receita.objects.get(pk=id)
    return render(request, 'blog/generic.html', {'receita': receita})

def construction(request):
    return render(request, 'blog/construction.html')

@login_required(login_url="/contas/login/")
def sobre(request):
        return render(request, 'blog/sobre.html')

@login_required(login_url="/contas/login/")
def livro(request):
    return render(request, 'blog/livro.html')

def receitas(request):
    filtro = BuscaFilter(request.GET, queryset=Receita.objects.all().order_by('-published_date'))

    return render(request, 'blog/receitas.html', {'filter': filtro})

@login_required(login_url="/contas/login/")
def new_recipe(request):
    if request.method == "POST":
        form = PostRecipe(request.POST, request.FILES)
        if form.is_valid():
            receitas = form.save(commit=False)
            receitas.author = request.user
            receitas.published_date = timezone.now()
            receitas.image = form.cleaned_data['image']
            receitas.save()
            return redirect('home_page')
    else:
        form = PostRecipe()
    return render(request, 'blog/new_recipe.html', {'form': form})

@login_required(login_url="/contas/login/")
def edit_recipe(request, id=None):
    receitas = get_object_or_404(Receita, id=id)
    if request.method == "POST":
        form = PostRecipe(request.POST, request.FILES, instance=receitas)
        if form.is_valid():
            receitas = form.save(commit=False)
            receitas.author = request.user
            receitas.published_date = timezone.now()
            receitas.image = form.cleaned_data['image']
            receitas.save()
            return redirect('generic', id=receitas.id)
    else:
        form = PostRecipe(instance=receitas)
    return render(request, 'blog/edit_recipe.html', {'form': form})