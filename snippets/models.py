from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from pygments import lexers


""" ----------------------------------------------------------------------
Getting the list of all languages supported by pygmest, to put them in a
choices in the slug field
--------------------------------------------------------------------- """
lista = list(lexers.get_all_lexers())
lista_first = [x[0].replace(" ", "").strip() for x in lista]
tupla = [(x, x) for x in lista_first]
LANGUAGES = tupla



class Language(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(choices=LANGUAGES, max_length=50)

    def __str__(self):
        return self.name


class Snippet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    snippet = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)
