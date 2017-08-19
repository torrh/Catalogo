# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Categoria, Comentario, Especie, Usuario

admin.site.register(Categoria)
admin.site.register(Especie)
admin.site.register(Comentario)
admin.site.register(Usuario)
