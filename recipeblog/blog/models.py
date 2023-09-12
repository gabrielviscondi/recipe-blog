from django.conf import settings
from django.db import models
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey

class Tipo(models.Model):
    name = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Categoria(models.Model):
    name = models.CharField(max_length=200)
    id_tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE, default=1)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Receita(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=60)
    ingredients = models.TextField()
    instructions = models.TextField()
    hints = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    id_tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE, default=1)
    id_categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, default=1)
    id_categoria = ChainedForeignKey(
        Categoria,
        chained_field="id_tipo",
        chained_model_field="id_tipo",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    image = models.ImageField(upload_to = 'receitas/', default = 'receitas/noimg.jpg')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name



