# Generated by Django 3.1.1 on 2022-11-09 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0032_auto_20221003_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='listaEspera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaSoli', models.DateField(blank=True, null=True)),
                ('telefono', models.CharField(blank=True, max_length=30, null=True)),
                ('turno', models.CharField(blank=True, max_length=30, null=True)),
                ('referencia', models.CharField(blank=True, max_length=60, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=120, null=True)),
                ('estado', models.BooleanField()),
                ('cas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asistencial.cas')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asistencial.paciente')),
            ],
        ),
    ]
