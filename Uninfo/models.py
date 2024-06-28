from django.db import models

class Universidade(models.Model):
    nome_completo = models.CharField(max_length=200)
    sigla = models.CharField(max_length=25)
    logo = models.URLField(default='https://example.com/seu-logo.png')
    local = models.CharField(max_length=500,blank=True)
    
    def __str__(self):
        return self.sigla
    
class Inscrito(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=50,)
    def __str__(self):
      return str(self.nome)
        
class TipoAtividade(models.Model):
    nome = models.CharField(max_length=50,default='Insira o tipo')

    def __str__(self):
        return self.nome

class PalavraChave(models.Model):
    palavra = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.palavra

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
        
class Curso(models.Model):
    nome=models.CharField(max_length=200)
    duracao=models.CharField(max_length=20,choices={'1 ano':'1 ano','2 anos':'2 anos','3 anos':'3 anos','4 anos':'4 anos','5 anos':'5 anos','6 anos':'6 anos', '7 anos':'7 anos', '8 anos':'8 anos', '9 anos':'9 anos', '10 anos':'10 anos'})
    


    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome=models.CharField(max_length=300)
    local=models.CharField(max_length=300,blank=True)

    def __str__(self):
        return self.nome
        
class Instituicao(models.Model):
    nome=models.CharField(max_length=200)
    local=models.CharField(max_length=500)
    pagina_oficial=models.URLField(max_length=2000)
    tipo = models.CharField(max_length=50,choices={'banco':'Banco','fundo_investimentos': 'Fundo de Investimentos','empresa  tecnologia':'Empresa de Tecnologia','laboratorio': 'Laboratório','construtora': 'Construtora','fabrica': 'Fábrica','escola': 'Escola','universidade': 'Universidade','hospital': 'Hospital','clinica': 'Clínica','ong': 'ONG','escritorio_advocacia': 'Escritório de Advocacia','escritorio_contabilidade': 'Escritório de Contabilidade','consultoria':'Consultoria','agencia_publicidade': 'Agência de Publicidade','agencia_viagens': 'Agência de Viagens','agencia_emprego': 'Agência de Emprego','agencia_noticias': 'Agência de Notícias','creche': 'Creche','orfanato': 'Orfanato','casa_repouso': 'Casa de Repouso','casa_cambio': 'Casa de Câmbio','outros': 'Outros'})
    
    def __str__(self):
        return self.nome


class Atividade(models.Model):
    nome = models.CharField(max_length=100)
    universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE)
    tipo_atividade = models.ForeignKey(TipoAtividade, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=20000)
    email_contato = models.EmailField(default='exemplo@gmail.com')
    link_instagram = models.URLField(blank=True)
    link_linkedin = models.URLField(blank=True)
    link_facebook = models.URLField(blank=True)
    link_site_oficial = models.URLField(blank=True)
    link_imagem = models.URLField(default='link da imagem')
    favorita = models.BooleanField(default=False)
    atividade_remunerada = models.BooleanField(default=False)
    fornece_bolsa = models.BooleanField(default=False)
    publico_alvo = models.CharField(max_length=500, blank=True)
    comentarios = models.TextField(max_length=10000,blank=True)
    local = models.CharField(max_length=500, blank=True, default='Local da sede, escritório etc')
    duracao = models.CharField(max_length=500, blank=True)
    requisitos = models.TextField(max_length=10000,blank=True)
    palavras_chave = models.ManyToManyField(PalavraChave, blank=True)
    pessoas_responsaveis = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    instituicoes_associadas = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    eventos = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

