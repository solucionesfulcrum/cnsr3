# Generated by Django 3.1.1 on 2021-10-27 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0013_auto_20211027_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provmaq',
            name='paciente',
        ),
        migrations.AddField(
            model_name='provmaq',
            name='bienpat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Asistencial.bienpat'),
            preserve_default=False,
        ),
    ]