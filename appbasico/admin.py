from django.contrib import admin

from .models import Equipe

admin.site.register(Equipe)

from .models import Postagem

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'post', 'slug')
