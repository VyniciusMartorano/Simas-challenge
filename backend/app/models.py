from django.db import models




class Estado(models.Model):
    uf = models.CharField(max_length=255,verbose_name='uf_estado')
    nome = models.CharField(max_length=255,verbose_name='nome_estado')
    

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']




class Cidade(models.Model):
    id_uf = models.ForeignKey(Estado, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255,verbose_name='nome_cidade')
    nome_uf = models.CharField(max_length=100, blank=True)


    def __str__(self):
        
        return self.nome
        
    class Meta:
        ordering = ['nome']




