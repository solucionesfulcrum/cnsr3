# Generated by Django 3.1.1 on 2021-10-28 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0015_remove_provmaq_bienpat'),
    ]

    operations = [
        migrations.AddField(
            model_name='provmaq',
            name='paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Asistencial.paciente'),
            preserve_default=False,
        ),
    ]