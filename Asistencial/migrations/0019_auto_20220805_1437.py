# Generated by Django 3.1.1 on 2022-08-05 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0018_auto_20220805_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegacionbienesestra',
            name='monto',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
