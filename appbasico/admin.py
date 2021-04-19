from django.contrib import admin

from .models import Equipe

from .models import Postagem

admin.site.register(Equipe)

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('time', 'nome', 'post','criado','modificado','ativo')
