from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .base_model import BaseModel
from django.db import models
from .publication import Publication


from .magazine import Magazine
from .reporter import Reporter


class Article(BaseModel):
    titulo = models.CharField(max_length=50,
                              verbose_name="Title",
                              help_text="Insira o titulo da reportagem.")

    pub_date = models.DateField(verbose_name="Published in")
    reporter = models.ForeignKey(Reporter, on_delete=models.RESTRICT)
    magazines = models.ManyToManyField(Magazine, verbose_name="Magazines", null=True, blank=True, through="Publication",through_fields=("article","magazine"))

    def __str__(self):
        return f"{self.titulo} by {self.reporter.name if self.reporter is not None else ''}"

    def clean(self):
        today = date.today()

        if self.pub_date > today:
            raise ValidationError(
                {"pub_date":_("A publication date must be in the future")},
            )