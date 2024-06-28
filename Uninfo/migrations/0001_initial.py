# Generated by Django 5.0.2 on 2024-06-11 03:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('duracao', models.CharField(choices=[('1 ano', '1 ano'), ('2 anos', '2 anos'), ('3 anos', '3 anos'), ('4 anos', '4 anos'), ('5 anos', '5 anos'), ('6 anos', '6 anos'), ('7 anos', '7 anos'), ('8 anos', '8 anos'), ('9 anos', '9 anos'), ('10 anos', '10 anos')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('local', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Inscrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('local', models.CharField(max_length=500)),
                ('pagina_oficial', models.URLField(max_length=2000)),
                ('tipo', models.CharField(choices=[('banco', 'Banco'), ('fundo_investimentos', 'Fundo de Investimentos'), ('empresa  tecnologia', 'Empresa de Tecnologia'), ('laboratorio', 'Laboratório'), ('construtora', 'Construtora'), ('fabrica', 'Fábrica'), ('escola', 'Escola'), ('universidade', 'Universidade'), ('hospital', 'Hospital'), ('clinica', 'Clínica'), ('ong', 'ONG'), ('escritorio_advocacia', 'Escritório de Advocacia'), ('escritorio_contabilidade', 'Escritório de Contabilidade'), ('consultoria', 'Consultoria'), ('agencia_publicidade', 'Agência de Publicidade'), ('agencia_viagens', 'Agência de Viagens'), ('agencia_emprego', 'Agência de Emprego'), ('agencia_noticias', 'Agência de Notícias'), ('creche', 'Creche'), ('orfanato', 'Orfanato'), ('casa_repouso', 'Casa de Repouso'), ('casa_cambio', 'Casa de Câmbio'), ('outros', 'Outros')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PalavraChave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palavra', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('contato', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoAtividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='Insira o tipo', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Universidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=200)),
                ('sigla', models.CharField(max_length=25)),
                ('logo', models.URLField(default='https://example.com/seu-logo.png')),
                ('local', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=20000)),
                ('email_contato', models.EmailField(default='exemplo@gmail.com', max_length=254)),
                ('link_instagram', models.URLField(blank=True)),
                ('link_linkedin', models.URLField(blank=True)),
                ('link_facebook', models.URLField(blank=True)),
                ('link_site_oficial', models.URLField(blank=True)),
                ('link_imagem', models.URLField(default='link da imagem')),
                ('favorita', models.BooleanField(default=False)),
                ('atividade_remunerada', models.BooleanField(default=False)),
                ('fornece_bolsa', models.BooleanField(default=False)),
                ('publico_alvo', models.CharField(blank=True, max_length=500)),
                ('comentarios', models.TextField(blank=True, max_length=10000)),
                ('local', models.CharField(blank=True, default='Local da sede, escritório etc', max_length=500)),
                ('duracao', models.CharField(blank=True, max_length=500)),
                ('requisitos', models.TextField(blank=True, max_length=10000)),
                ('eventos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Uninfo.evento')),
                ('instituicoes_associadas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Uninfo.instituicao')),
                ('palavras_chave', models.ManyToManyField(blank=True, to='Uninfo.palavrachave')),
                ('pessoas_responsaveis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Uninfo.pessoa')),
                ('tipo_atividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Uninfo.tipoatividade')),
                ('universidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Uninfo.universidade')),
            ],
        ),
    ]