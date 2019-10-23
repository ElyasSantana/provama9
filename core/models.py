from django.db import models


class Cliente(models.Model):
    foto = models.FileField(upload_to='cliente_image', blank=True)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=10)
    telefone = models.CharField(max_length=12)

    def __str__(self):
        return '%s %s' % (self.nome, self.sobrenome)


class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente,
                                on_delete=models.CASCADE,
                                related_name='enderecos')
    logradouro = models.CharField(max_length=80)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    numero = models.CharField(max_length=20)
