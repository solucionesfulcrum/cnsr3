# Generated by Django 3.1.1 on 2022-03-16 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0048_personalvpn_personalautoriza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalvpn',
            name='fechaHabilita',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='personalvpn',
            name='fecha_reg',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalvpn',
            name='ip',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='personalCertificado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaSolicita', models.DateField()),
                ('tipoCertificado', models.CharField(max_length=30)),
                ('fechaInstalacion', models.DateField(null=True)),
                ('perosnalInstala', models.CharField(max_length=40, null=True)),
                ('observacion', models.CharField(max_length=200, null=True)),
                ('fecha_reg', models.DateTimeField(auto_now=True)),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asistencial.personal')),
            ],
        ),
    ]