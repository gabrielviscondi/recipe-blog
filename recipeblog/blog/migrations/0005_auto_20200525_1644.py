# Generated by Django 2.2.12 on 2020-05-25 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200525_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id_tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Tipo'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='id_tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Tipo'),
        ),
    ]
