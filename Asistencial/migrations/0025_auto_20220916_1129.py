# Generated by Django 3.1.1 on 2022-09-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0024_auto_20220915_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maestromatsap',
            name='desProducto',
            field=models.CharField(max_length=200),
        ),
    ]
