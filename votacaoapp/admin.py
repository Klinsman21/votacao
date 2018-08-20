from django.contrib import admin

from .models import Votacao, Votadas, Comments


class VotacaoAdmin(admin.ModelAdmin):

  list_display = ['nome', 'description', 'votoSim', 'votoNao','inicial_time','final_time']

class VotadasAdmin(admin.ModelAdmin):

  list_display = ['userId', 'leiId']

class CommentsAdmin(admin.ModelAdmin):

  list_display = ['comentario', 'leiId']

admin.site.register(Votacao)
admin.site.register(Votadas)
admin.site.register(Comments)
# Register your models here.
