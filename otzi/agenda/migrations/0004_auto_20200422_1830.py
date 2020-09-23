# Generated by Django 3.0.5 on 2020-04-22 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_auto_20200407_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracaoagenda',
            name='dia',
            field=models.CharField(choices=[('', ''), ('segunda', 'Segunda'), ('terca', 'Terça'), ('quarta', 'Quarta'), ('quinta', 'Quinta'), ('sexta', 'Sexta'), ('sabado', 'Sábado'), ('domingo', 'Domingo'), ('feriado_religioso', 'Feriados Religiosos')], default='', max_length=17, verbose_name='Dia'),
        ),
        migrations.AlterField(
            model_name='configuracaoagenda',
            name='horario_inicio',
            field=models.CharField(choices=[('', ''), ('nulo', 'Não informar.'), ('00:00', '00:00'), ('01:00', '01:00'), ('02:00', '02:00'), ('03:00', '03:00'), ('04:00', '04:00'), ('05:00', '05:00'), ('06:00', '06:00'), ('07:00', '07:00'), ('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00')], default='08:00', max_length=5, verbose_name='Inicio de Expediente'),
        ),
        migrations.AlterField(
            model_name='configuracaoagenda',
            name='horario_inicio_almoco',
            field=models.CharField(blank=True, choices=[('', ''), ('nulo', 'Não informar.'), ('00:00', '00:00'), ('01:00', '01:00'), ('02:00', '02:00'), ('03:00', '03:00'), ('04:00', '04:00'), ('05:00', '05:00'), ('06:00', '06:00'), ('07:00', '07:00'), ('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00')], default='12:00', max_length=5, null=True, verbose_name='Pausa para o Almoço'),
        ),
        migrations.AlterField(
            model_name='configuracaoagenda',
            name='horario_termino',
            field=models.CharField(choices=[('', ''), ('nulo', 'Não informar.'), ('00:00', '00:00'), ('01:00', '01:00'), ('02:00', '02:00'), ('03:00', '03:00'), ('04:00', '04:00'), ('05:00', '05:00'), ('06:00', '06:00'), ('07:00', '07:00'), ('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00')], default='18:00', max_length=5, verbose_name='Encerramento do Expediente'),
        ),
        migrations.AlterField(
            model_name='configuracaoagenda',
            name='horario_termino_almoco',
            field=models.CharField(blank=True, choices=[('', ''), ('nulo', 'Não informar.'), ('00:00', '00:00'), ('01:00', '01:00'), ('02:00', '02:00'), ('03:00', '03:00'), ('04:00', '04:00'), ('05:00', '05:00'), ('06:00', '06:00'), ('07:00', '07:00'), ('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00')], default='14:00', max_length=5, null=True, verbose_name='Termino da Pausa do Almoço'),
        ),
        migrations.AlterField(
            model_name='horarioagendado',
            name='horario',
            field=models.CharField(choices=[('', ''), ('nulo', 'Não informar.'), ('00:00', '00:00'), ('01:00', '01:00'), ('02:00', '02:00'), ('03:00', '03:00'), ('04:00', '04:00'), ('05:00', '05:00'), ('06:00', '06:00'), ('07:00', '07:00'), ('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00')], default='00:00', max_length=5, verbose_name='Horario'),
        ),
    ]