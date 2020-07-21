from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Aqui criamos os campos das nossas tabela sql
#python manage.py makemigrations core 0001 e depois:
#python manage.py slqmigrate core e por fim
#python manage.py migrate core 0001
#depois é só registra-lo no Django admin
class Evento(models.Model):
    titulo = models.CharField(max_length = 100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name= 'Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True) #sera automatico
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    #quando excluir a  pessoa todos os eventos dela serão excluidos
    #se modifico uma classe preciso aplicar isso ao bd use:
    #python manage.py makemigrations core que checa se existem alterações
    #depois use python manage.py sqlmigrate core 0002
    #python manage.py migrate core 0002

    class Meta:
        db_table = 'evento' #o nome da nossa tabela será evento, Caso a tabela já esteja criada é só deletar

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')
