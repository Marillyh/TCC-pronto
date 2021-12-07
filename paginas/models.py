from django.db import models

class Produto(models.Model):
	titulo = models.CharField(max_length=50)
	imagem = models.FileField(upload_to='media')
	tamanho = models.CharField(max_length=2)
	descricao = models.CharField(max_length=300)
	preco = models.DecimalField(decimal_places=2, max_digits=6, default=0.00)

  #python 3
def _str_ (self):
    return self.titulo



