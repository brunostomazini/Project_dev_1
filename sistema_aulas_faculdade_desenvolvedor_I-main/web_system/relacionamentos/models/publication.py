from . import  article
from .base_model import BaseModel
from .magazine import Magazine
from .person import Person
from django.db import models

class Publication(BaseModel):
    magazine = models.ForeignKey('Magazine', on_delete=models.RESTRICT)
    article = models.ForeignKey('article', on_delete=models.RESTRICT)
    editor = models.ForeignKey('Person', on_delete=models.RESTRICT)
    #date = models.DateField()
    #obs =  models.TextFile()

    def __str__(self):
        return f'{self.magazine}: {self.article} edited by {self.editor} at {self.date}'