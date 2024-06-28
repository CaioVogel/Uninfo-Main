from django.contrib import admin
from .models import Universidade, Atividade, TipoAtividade, PalavraChave, Pessoa, Curso, Evento, Instituicao 

class UniversidadeAdmin(admin.ModelAdmin):
  list_display = ['nome_completo', 'sigla', 'logo']
  ordering = ['nome_completo']

admin.site.register(Universidade, UniversidadeAdmin)


class AtividadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'universidade', 'tipo_atividade', 'descricao', 'email_contato', 'link_instagram', 'link_linkedin', 'link_facebook', 'link_site_oficial', 'link_imagem', 'favorita', 'atividade_remunerada', 'fornece_bolsa', 'publico_alvo', 'comentarios', 'local', 'duracao', 'requisitos', 'display_palavras_chave', 'pessoas_responsaveis', 'instituicoes_associadas', 'eventos']
    ordering = ['nome']

    # Método para exibir as palavras-chave
    def display_palavras_chave(self, obj):
        return ', '.join([palavra.palavra for palavra in obj.palavras_chave.all()])

    # Definindo a ordenação por palavras-chave
    display_palavras_chave.admin_order_field = 'palavras_chave__palavra'

    # Renomeando a coluna exibida no admin
    display_palavras_chave.short_description = 'Palavras-Chave'

admin.site.register(Atividade, AtividadeAdmin)

class TipoAtividadeAdmin(admin.ModelAdmin):
  list_display = ['nome']
  ordering = ['nome']

admin.site.register(TipoAtividade, TipoAtividadeAdmin) 

class PalavraChaveAdmin(admin.ModelAdmin):
  list_display = ['palavra']
  ordering = ['palavra']

admin.site.register(PalavraChave, PalavraChaveAdmin)

class PessoaAdmin(admin.ModelAdmin):
  list_display = ['nome', 'contato']
  ordering = ['nome']

admin.site.register(Pessoa, PessoaAdmin)

class CursoAdmin(admin.ModelAdmin):
  list_display = ['nome', 'duracao']
  ordering = ['nome']

admin.site.register(Curso, CursoAdmin)

class EventoAdmin(admin.ModelAdmin):
  list_display = ['nome', 'local']
  ordering = ['nome']

admin.site.register(Evento, EventoAdmin)

class InstituicaoAdmin(admin.ModelAdmin):
  list_display = ['nome', 'local','pagina_oficial','tipo']
  ordering = ['nome']

admin.site.register(Instituicao, InstituicaoAdmin)

