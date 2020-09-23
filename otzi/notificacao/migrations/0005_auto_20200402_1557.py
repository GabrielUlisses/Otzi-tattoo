# Generated by Django 3.0.3 on 2020-04-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificacao', '0004_auto_20200402_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacao',
            name='visto',
            field=models.BooleanField(blank=True, default='False', null=True, verbose_name='Vizualizada'),
        ),
        migrations.AlterField(
            model_name='notificacao',
            name='conteudo',
            field=models.TextField(max_length=260, verbose_name='Conteúdo'),
        ),
        migrations.AlterField(
            model_name='notificacao',
            name='titulo',
            field=models.CharField(max_length=60, verbose_name='Título'),
        ),
    ]