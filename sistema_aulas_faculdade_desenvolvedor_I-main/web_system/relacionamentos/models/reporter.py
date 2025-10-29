from relacionamentos.managers.reporter_manager import ReporterManager
from .base_model import BaseModel
from django.db import models
from relacionamentos.validators import validate_cpf
from django.core.validators import MinLengthValidator



class Reporter(BaseModel):
    name = models.CharField(max_length=100,
                            verbose_name="Reporter",
                            help_text="Reporter name")
    cpf = models.CharField(max_length=11,
                           validators=[validate_cpf])
    email = models.EmailField(max_length=255,)

    def __str__(self):
        return self.name


    objects = ReporterManager

