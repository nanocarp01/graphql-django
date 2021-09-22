from django.db import models

class API(models.Model):
    id = models.IntegerField(primary_key=True)
    legajo = models.FloatField()
    agente = models.CharField(max_length=100)
    secretaria = models.CharField(max_length=100)
    

    def __str__(self):
        return  self.agente