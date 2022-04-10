from django.contrib import admin

from .models import Cidade, Estado

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id','uf','nome',)
    list_display_links = ('id', 'nome',)


class CidadeAdmin(admin.ModelAdmin):
    list_display = ('id','id_uf','nome','nome_uf')
    list_display_links = ('id', 'nome',)


admin.site.register(Cidade,CidadeAdmin)
admin.site.register(Estado, EstadoAdmin)
