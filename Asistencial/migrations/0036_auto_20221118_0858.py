# Generated by Django 3.1.1 on 2022-11-18 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0035_docucontratados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docucontratados',
            name='fecha_reg',
            field=models.DateField(auto_now=True),
        ),
    ]
