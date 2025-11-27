from django.db import models

class Operations(models.TextChoices):
    ADDITION = "+", "Adição"
    SUBTRACTION = "-", "Subtração"
    MULTIPLICATION = "*", "Multiplicação"
    DIVISION = "/", "Divisão"