# Generated by Django 4.0.3 on 2022-04-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_estado_nome_uf_cidade_nome_uf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='nome_uf',
            field=models.CharField(max_length=100),
        ),
    ]
