from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Receita
from .forms import PostRecipe

def post_list(request):
    receitas = Receita.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:9]
    return render(request, 'blog/post_list.html', {'receitas': receitas})

def generic(request, id):
    receita = Receita.objects.get(pk=id)
    return render(request, 'blog/generic.html', {'receita': receita})

def construction(request):
        return render(request, 'blog/construction.html')
        
def receitas(request):
    receitas = Receita.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/receitas.html', {'receitas': receitas})

def new_recipe(request):
    if request.method == "POST":
        form = PostRecipe(request.POST)
        if form.is_valid():
            receitas = form.save(commit=False)
            receitas.author = request.user
            receitas.published_date = timezone.now()
            receitas.save()
            return redirect('post_list')
                    
            fields = ('name', 'short_desc','ingredients','instructions','hints', 'image')


    else:
        form = PostRecipe()
    return render(request, 'blog/new_recipe.html', {'form': form})   