

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    """Uma receita criada pelo usuário (ex: Lasanha, Salada Grega)."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(help_text="Modo de preparo ou ingredientes.")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MealPlan(models.Model):
    """
    Representa um dia específico no plano de refeições.
    Conecta uma receita a um dia e um período (café, almoço, jantar).
    """
    DAYS_OF_WEEK = [
        ('seg', 'Segunda-feira'),
        ('ter', 'Terça-feira'),
        ('qua', 'Quarta-feira'),
        ('qui', 'Quinta-feira'),
        ('sex', 'Sexta-feira'),
        ('sab', 'Sábado'),
        ('dom', 'Domingo'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    
    # Ex: Café da manhã, Almoço, Jantar
    meal_type = models.CharField(max_length=20, default='Almoço') 

    class Meta:
        verbose_name_plural = 'meal plans'

    def __str__(self):
        return f"{self.day} - {self.meal_type}: {self.recipe.name}"	
