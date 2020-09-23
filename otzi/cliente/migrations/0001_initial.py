# Generated by Django 3.0.3 on 2020-03-22 00:55

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tatuador', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('ultima_modificacao', models.DateTimeField(auto_now=True, verbose_name='Última Modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('especializacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.Especializacao')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='PedidoOrcamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('ultima_modificacao', models.DateTimeField(auto_now=True, verbose_name='Última Modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('titulo', models.CharField(max_length=20, verbose_name='Titulo')),
                ('texto_receptivo', models.CharField(max_length=100, verbose_name='Recepção')),
                ('parte_corpo', models.CharField(max_length=20, verbose_name='Parte do corpo')),
                ('img_1', stdimage.models.StdImageField(blank=True, null=True, upload_to='cliente/pedido_orcamento/')),
                ('img_2', stdimage.models.StdImageField(blank=True, null=True, upload_to='cliente/pedido_orcamento/')),
                ('img_3', stdimage.models.StdImageField(blank=True, null=True, upload_to='cliente/pedido_orcamento/')),
                ('tamanho', models.CharField(default='Altura: 40cm x Largura: 20cm ', max_length=40, verbose_name='Tamanho')),
                ('texto_complementar', models.TextField(max_length=300, verbose_name='Especificações e Descrição')),
                ('preco_esperado', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor esperado')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.Cliente')),
                ('tatuadores', models.ManyToManyField(limit_choices_to=6, to='tatuador.Tatuador')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]