# Generated by Django 4.0.3 on 2022-04-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_cidade_id_alter_estado_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='nome_uf',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
