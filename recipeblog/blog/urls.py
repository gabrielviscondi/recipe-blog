from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('receitas/nova/', views.new_recipe, name='new_recipe'),
    path('receitas/editar/<int:id>', views.edit_recipe, name='edit_recipe'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)