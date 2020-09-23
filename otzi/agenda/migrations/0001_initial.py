# Generated by Django 3.0.3 on 2020-03-22 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tatuador', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('ultima_modificacao', models.DateTimeField(auto_now=True, verbose_name='Última Modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('tatuador', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='tatuador.Tatuador')),
            ],
            options={
                'ordering': ['tatuador', 'data_criacao'],
            },
        ),
        migrations.CreateModel(
            name='ConfiguracaoAgenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('ultima_modificacao', models.DateTimeField(auto_now=True, verbose_name='Última Modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('dia', models.CharField(choices=[('', ''), ('Segunda', 'segunda'), ('Terça', 'terca'), ('Quarta', 'quarta'), ('Quinta', 'quinta'), ('Sexta', 'sexta'), ('Sábado', 'sabado'), ('Domingo', 'domingo'), ('Feriado Nacional', 'feriado_nacional'), ('Feriado Religioso', 'feriado_religioso')], default='', max_length=17, verbose_name='Dia')),
                ('horario_inicio', models.CharField(choices=[('', ''), ('00:00', '00:00'), ('00:30', '00:30'), ('01:00', '01:00'), ('01:30', '01:30'), ('02:00', '02:00'), ('02:30', '02:30'), ('03:00', '03:00'), ('03:30', '03:30'), ('04:00', '04:00'), ('04:30', '04:30'), ('05:00', '05:00'), ('05:30', '05:30'), ('06:00', '06:00'), ('06:30', '06:30'), ('07:00', '07:00'), ('07:30', '07:30'), ('08:00', '08:00'), ('08:30', '08:30'), ('09:00', '09:00'), ('09:30', '09:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00'), ('21:30', '21:30'), ('22:00', '22:00'), ('22:30', '22:30'), ('11:00', '11:00'), ('11:30', '11:30')], default='08:00', max_length=5, verbose_name='Inicio de Expediente')),
                ('horario_termino', models.CharField(choices=[('', ''), ('00:00', '00:00'), ('00:30', '00:30'), ('01:00', '01:00'), ('01:30', '01:30'), ('02:00', '02:00'), ('02:30', '02:30'), ('03:00', '03:00'), ('03:30', '03:30'), ('04:00', '04:00'), ('04:30', '04:30'), ('05:00', '05:00'), ('05:30', '05:30'), ('06:00', '06:00'), ('06:30', '06:30'), ('07:00', '07:00'), ('07:30', '07:30'), ('08:00', '08:00'), ('08:30', '08:30'), ('09:00', '09:00'), ('09:30', '09:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00'), ('21:30', '21:30'), ('22:00', '22:00'), ('22:30', '22:30'), ('11:00', '11:00'), ('11:30', '11:30')], default='18:00', max_length=5, verbose_name='Encerramento do Expediente')),
                ('horario_inicio_almoco', models.CharField(blank=True, choices=[('', ''), ('00:00', '00:00'), ('00:30', '00:30'), ('01:00', '01:00'), ('01:30', '01:30'), ('02:00', '02:00'), ('02:30', '02:30'), ('03:00', '03:00'), ('03:30', '03:30'), ('04:00', '04:00'), ('04:30', '04:30'), ('05:00', '05:00'), ('05:30', '05:30'), ('06:00', '06:00'), ('06:30', '06:30'), ('07:00', '07:00'), ('07:30', '07:30'), ('08:00', '08:00'), ('08:30', '08:30'), ('09:00', '09:00'), ('09:30', '09:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00'), ('21:30', '21:30'), ('22:00', '22:00'), ('22:30', '22:30'), ('11:00', '11:00'), ('11:30', '11:30')], default='12:00', max_length=5, null=True, verbose_name='Pausa para o Almoço')),
                ('horario_termino_almoco', models.CharField(blank=True, choices=[('', ''), ('00:00', '00:00'), ('00:30', '00:30'), ('01:00', '01:00'), ('01:30', '01:30'), ('02:00', '02:00'), ('02:30', '02:30'), ('03:00', '03:00'), ('03:30', '03:30'), ('04:00', '04:00'), ('04:30', '04:30'), ('05:00', '05:00'), ('05:30', '05:30'), ('06:00', '06:00'), ('06:30', '06:30'), ('07:00', '07:00'), ('07:30', '07:30'), ('08:00', '08:00'), ('08:30', '08:30'), ('09:00', '09:00'), ('09:30', '09:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00'), ('21:30', '21:30'), ('22:00', '22:00'), ('22:30', '22:30'), ('11:00', '11:00'), ('11:30', '11:30')], default='14:00', max_length=5, null=True, verbose_name='Termino da Pausa do Almoço')),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agenda.Agenda')),
            ],
            options={
                'verbose_name': 'Configuração de Agenda',
                'verbose_name_plural': 'Configurações de Agenda',
            },
        ),
        migrations.CreateModel(
            name='HorarioAgendado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('ultima_modificacao', models.DateTimeField(auto_now=True, verbose_name='Última Modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('horario', models.CharField(choices=[('', ''), ('00:00', '00:00'), ('00:30', '00:30'), ('01:00', '01:00'), ('01:30', '01:30'), ('02:00', '02:00'), ('02:30', '02:30'), ('03:00', '03:00'), ('03:30', '03:30'), ('04:00', '04:00'), ('04:30', '04:30'), ('05:00', '05:00'), ('05:30', '05:30'), ('06:00', '06:00'), ('06:30', '06:30'), ('07:00', '07:00'), ('07:30', '07:30'), ('08:00', '08:00'), ('08:30', '08:30'), ('09:00', '09:00'), ('09:30', '09:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00'), ('21:30', '21:30'), ('22:00', '22:00'), ('22:30', '22:30'), ('11:00', '11:00'), ('11:30', '11:30')], default='00:00', max_length=5, verbose_name='Horario')),
                ('data', models.DateTimeField(verbose_name='Data do Agendamento')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.Cliente', verbose_name='Cliente')),
                ('configuracao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agenda.ConfiguracaoAgenda', verbose_name='Configuração Agenda')),
            ],
            options={
                'verbose_name': 'Horario Agendado',
                'verbose_name_plural': 'Horarios Agendados',
                'ordering': ['data_criacao', 'cliente'],
            },
        ),
        migrations.CreateModel(
            name='ConclusaoTatuador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('ultima_modificacao', models.DateTimeField(auto_now=True, verbose_name='Última Modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('critica', models.TextField(max_length=150, verbose_name='Crítica')),
                ('cliente_presente', models.BooleanField(default=True, verbose_name='Cliente Compareceu?')),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agenda.HorarioAgendado')),
            ],
            options={
                'verbose_name': 'Conclusão Tatuador',
                'verbose_name_plural': 'Conclusões Tatuadores',
                'ordering': ['data_criacao'],
            },
        ),
        migrations.CreateModel(
            name='ConclusaoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('ultima_modificacao', models.DateTimeField(auto_now=True, verbose_name='Última Modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('critica', models.TextField(max_length=150, verbose_name='Crítica')),
                ('aprovado', models.BooleanField(default=True, verbose_name='Gostou?')),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agenda.HorarioAgendado')),
            ],
            options={
                'verbose_name': 'Conclusão Cliente',
                'verbose_name_plural': 'Conclusões Clientes',
                'ordering': ['data_criacao'],
            },
        ),
    ]