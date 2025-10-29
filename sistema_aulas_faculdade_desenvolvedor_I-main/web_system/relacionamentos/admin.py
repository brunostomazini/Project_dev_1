from django.contrib import admin
from relacionamentos.models import Person
from relacionamentos.models import Magazine
from relacionamentos.models import Reporter
from relacionamentos.models import Article

# Register your models here.

admin.site.register(Person)
admin.site.register(Magazine)
admin.site.register(Reporter)
admin.site.register(Article)
