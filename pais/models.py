from django.db import models

# Create your models here.
class Country(models.Model):
    FIRST_LEVEL_CHOICES = [
        ("Estado", "Estado"),
        ("Provincias", "Provincias"),
        ("Regiones", "Regiones"),
    ]

    SECOND_LEVEL_CHOICES = [
        ("Municipios", "Municipios"),
        ("Condados", "Condados"),
        ("Distritos", "Distritos"),
    ]


    # first level administrative division
    nome = models.CharField(max_length=100)
    first_level = models.CharField(
        max_length=100, 
        choices=FIRST_LEVEL_CHOICES, 
        blank=True, 
        null=True
    ) 

    # second level administrative division
    second_level = models.CharField(
        max_length=100, 
        choices=SECOND_LEVEL_CHOICES, 
        blank=True, 
        null=True
    )

    
    def __str__(self):
        return self.nome
    
class State(models.Model):
    nome = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    

class Municipality(models.Model):
    nome = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    

