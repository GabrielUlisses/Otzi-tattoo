# Generated by Django 3.0.3 on 2020-06-13 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notificacao', '0010_notificacao_destinatarios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificacaousuario',
            old_name='notificao',
            new_name='notificacao',
        ),
    ]
